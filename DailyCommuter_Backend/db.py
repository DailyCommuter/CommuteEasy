import sqlite3
from datetime import datetime
from google.transit import gtfs_realtime_pb2
import click
import config
import os
from dotenv import load_dotenv
from flask import current_app, g

import requests


# URLs for all api calls
train_update_urls = [
    config.ACESR_FEED_URL,
    config.BDFM_FEED_URL,
    config.G_FEED_URL,
    config.NQRW_FEED_URL,
    config.L_FEED_URL,
    config.NUMBERS_AND_S_FEED_URL,
    config.SIR_FEED_URL,]

service_alert_urls = [
    config.ALL_SERVICE_ALERTS_URL_GTFS,
    config.SUBWAY_ALERTS_URL_GTFS,
    config.BUS_ALERTS_URL_GTFS,
    config.LIRR_ALERTS_URL_GTFS,
    config.METRO_NORTH_ALERTS_URL_GTFS]

elev_escal_json_urls = [
    config.ELEV_ESCAL_CURRENT_OUTAGES_JSON,
    config.ELEV_ESCAL_UPCOMING_OUTAGES_JSON,
    config.ELEV_ESCAL_EQUIPMENTS_OUTAGES_JSON,]

# The bus api still requires an api key, thus the need for dotenv
# API key must be given to server when deploying
load_dotenv()
BUS_FEED_KEY = os.getenv("BUS_FEED_KEY")


def fetch_data(endpoint, key=None):
    feed = gtfs_realtime_pb2.FeedMessage()
    if key is None:
        response = requests.get(endpoint)
        feed.ParseFromString(response.content)
    else:
        response = requests.get(f"{endpoint}key={key}")
        feed.ParseFromString(response.content)
    return feed


# Train update GTFS structure is as follows:
'''
Has 2 types of entities:
trip_update (if there is a delay etc) which contains:
    trip
    stop_time_update (for each stop on the route_id)
vehicle (what stop it's currently at on this route_id) which contains:
    trip
    timestamp
    stop_id

Example:
----------------------------------
id: "000031FS"
trip_update {
    trip {
        trip_id: "111150_FS.S01R"
        start_time: "18:31:30"
        start_date: "20250324"
        route_id: "FS"
    }
    stop_time_update {
        arrival {
            time: 1742855490
        }
        departure {
            time: 1742855490
        }
        stop_id: "S01S"
    }

    ...

    stop_time_update {
        arrival {
            time: 1742855880
        }
        departure {
            time: 1742855880
        }
        stop_id: "D26S"
    }
} 
----------------------------------
id: "000030FS"
vehicle {
    trip {
        trip_id: "111100_FS.N01R"
        start_time: "18:31:00"
        start_date: "20250324"
        route_id: "FS"
    }
    timestamp: 1742855460
    stop_id: "D26N"
}
----------------------------------
'''
def update_trains(feed):
    try:
        with get_db() as db:
            trip_update_id = None
            for entity in feed.entity:
                # Check if update_id already exists (prevents duplicates)
                id_exists = db.execute(
                    "SELECT id FROM trip_update WHERE update_id = ?", 
                    (entity.id,)
                ).fetchone()

                if id_exists:
                    # print(f"Skipping duplicate update_id: {entity.id}")
                    continue
                
                # Get and store the trip info about the following updates
                if entity.HasField('trip_update'):
                    db.execute(
                        """
                        INSERT INTO trip_update 
                        (update_id, trip_id, start_tm, start_dt, route_id)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (entity.id,
                        entity.trip_update.trip.trip_id, 
                        entity.trip_update.trip.start_time, 
                        entity.trip_update.trip.start_date, 
                        entity.trip_update.trip.route_id,)
                    )

                    # Get id from the main trip_update table as reference 
                    # for stop_update and vehicle_update tables
                    trip_update_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]

                    # Get and store the actual updates info
                    for update in entity.trip_update.stop_time_update:
                        if trip_update_id is not None:
                            db.execute(
                                """
                                INSERT INTO stop_update 
                                (trip_update_id, arrival, departure, stop_id, direction)
                                VALUES (?, ?, ?, ?, ?)
                                """,
                                (trip_update_id,
                                update.arrival.time, 
                                update.departure.time, 
                                update.stop_id[:-1],
                                update.stop_id[-1],)
                            )

                # Get and store the vehecle info about the above updates
                if entity.HasField('vehicle'):
                    if trip_update_id is not None:
                        db.execute(
                            """
                            INSERT INTO vehicle_update
                            (trip_update_id, timestmp, curr_stop_id)
                            VALUES (?, ?, ?)
                            """,
                            (trip_update_id,
                            entity.vehicle.timestamp, 
                            entity.vehicle.stop_id,)
                        )
            db.commit()

    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
    except Exception as e:
        print(f"Error updating database: {e}")
    finally:
        pass


# Bus update GTFS structure is as follows:
def update_busses(feed):
    pass


# Elevator and escalator alert GTFS structure is as follows:
def update_elev_escal_alerts(feed):
    pass


# TODO double check that the individual service alert feeds 
#   are the same structure as the "All Service Alerts" feed
# Service alert GTFS structure is as follows:
'''
Example:
----------------------------------
id: "lmm:planned_work:19829"
alert {
  active_period {
    start: 1727755260
    end: 1727776800
  }
  ...
  ...
  ...
  active_period {
    start: 1758254460
    end: 1758276000
  }
  informed_entity {
    agency_id: "MTASBWY"
    route_id: "GS"
  }
  header_text {
    translation {
      text: "Take the [7] instead"
      language: "en"
    }
    translation {
      text: "<p>Take the [7] instead</p>"
      language: "en-html"
    agency_id: "MTASBWY"
    route_id: "GS"
  }
  header_text {
    translation {
      text: "Take the [7] instead"
      language: "en"
    }
    translation {
      text: "<p>Take the [7] instead</p>"
      language: "en-html"
    route_id: "GS"
  }
  header_text {
    translation {
      text: "Take the [7] instead"
      language: "en"
    }
    translation {
      text: "<p>Take the [7] instead</p>"
      language: "en-html"
  header_text {
    translation {
      text: "Take the [7] instead"
      language: "en"
    }
    translation {
      text: "<p>Take the [7] instead</p>"
      language: "en-html"
      text: "Take the [7] instead"
      language: "en"
    }
    translation {
      text: "<p>Take the [7] instead</p>"
      language: "en-html"
    translation {
      text: "<p>Take the [7] instead</p>"
      language: "en-html"
    }
  }
      language: "en-html"
    }
  }
  description_text {
    }
  }
  description_text {
  description_text {
    translation {
    translation {
      text: "[S] 42 St Shuttle operates daily during days and evenings.\n\nPlan your trip at mta.info or download the MTA app for iOS or Android.."
      text: "[S] 42 St Shuttle operates daily during days and evenings.\n\nPlan your trip at mta.info or download the MTA app for iOS or Android.."
      language: "en"
      language: "en"
    }
    }
    translation {
      text: "<p>[S] 42 St Shuttle operates daily during days and evenings.</p><p></p><p>Plan your trip at <a title=\"\" href=\"https://mta.info\" rel=\"noopener noreferrer nofollow\" data-link-auto=\"\" target=\"_blank\">mta.info</a> or download the MTA app for <a title=\"\" href=\"https://apps.apple.com/us/app/mymta/id1297605670\" rel=\"noopener noreferrer nofollow\" target=\"_blank\">iOS</a> or <a title=\"\" href=\"https://play.google.com/store/apps/details?id=info.mta.mymta&amp;hl=en_US&amp;gl=US\" rel=\"noopener noreferrer nofollow\" target=\"_blank\">Android</a>..</p>"
      language: "en-html"
    }
  }
}
'''
def update_service_alerts(feed):
    db = get_db()
    i = 0
    while i < 5:
        for entity in feed.entity:
            # Get and store the update_id
            db.execute(
                'INSERT INTO subway_alerts (alert_id)'
                'VALUES (?)',
                (entity.id,)
            )
            db.commit()
            # Get and store the actual alert
            if entity.HasField('alert'):
                # print(entity.alert.header_text.translation[0].text)
                # print('----------------------------------')
                db.execute(
                    'INSERT INTO subway_alerts (agency_id, route_id, alert_text)'
                    'VALUES (?, ?, ?)',
                    (entity.alert.informed_entity[0].agency_id, 
                    entity.alert.informed_entity[0].route_id,
                    entity.alert.header_text.translation[0].text,)
                )
                db.commit()
            # TODO add the description_text from the end of the entity. 
            #   not sure how to do that
            i += 1


def update_all_feeds():
    # Update all the trains
    for url in train_update_urls:
        update_trains(fetch_data(url))
    
    # TODO Complete update_busses() to get bus data
    
    # TODO Complete/confirm the update_service_alerts() function
    # Update all the alerts
    # for url in service_alert_urls:
    #     update_service_alerts(fetch_data(url))


# Find the SUBWAY stop that is closest to the given latitude and longitude
def closest_sub_stop(lat, lon):
    pass


# Find the BUS stop that is closest to the given latitude and longitude
def closest_bus_stop(lat, lon):
    pass


# Route:
#   Receive latitude and longitude from Front End, for both, the trip start, and trip end
#   Identify 2 stops that are closest to start and end
#   (Find all stops that are between the 2)
#   Get the arrival times of trains at start and end stops
#   Get the estimated travel time from start to end
def map_sub_route(start_lat, start_lon, end_lat, end_lon):
    start_stop = closest_sub_stop(start_lat, start_lon)
    end_stop = closest_sub_stop(end_lat, end_lon)
    pass


# for Gideok
def get_all_subway_stops():
    pass


'''
Functions for initialization and teardown of the app
'''
# Register close_db and init_db_command with the Application
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# Initialize the db
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    get_all_subway_stops()


# Set up the command 'init-db' for the Flask CLI
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


# Tell Python how to interpret timestamp values in the db
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)


# Connect the db with the running instance of the app and it receives a request
# Establish a connection to the file pointed at by the DATABASE configuration key
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row # act like a dict

    return g.db


# Close the db when finished with the request
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()