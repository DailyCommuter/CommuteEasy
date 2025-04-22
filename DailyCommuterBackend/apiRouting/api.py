import config
import os
import time
import datetime
import json
import requests
import sqlite3
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from flask import jsonify
from DailyCommuterBackend.db import get_db
from DailyCommuterBackend.models import Route


# API key must be given to server when deploying
load_dotenv()
BUS_FEED_KEY = os.getenv("BUS_FEED_KEY")
TRANSIT_TOKEN = os.getenv("TRANSIT_TOKEN")


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


def fetch_data(endpoint, key=None):
    feed = gtfs_realtime_pb2.FeedMessage()
    if key is None:
        response = requests.get(endpoint)
        if not response.status_code == 200:
            print(f"Failed to fetch data: {response.status_code}")
            return
        feed.ParseFromString(response.content)
    else:
        response = requests.get(f"{endpoint}key={key}")
        feed.ParseFromString(response.content)
    return feed


# Train update GTFS structure is as follows:
'''
Has 2 types of entities:
trip_update (if there is a delay etc) show information about the stops a train will make in the future (stopTimeUpdates)
Contains:
    trip
    stop_time_update (for each stop on the route_id)
vehicle (what stop it's currently at on this route_id) show information about the current status of the train
Contains:
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


def geocoder(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'DailyCommuter chz9577@nyu.edu'
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return lat, lon
    else:
        raise ValueError("Could not geocode address", address)


def createRoute(start_address, end_address, arriveby, userid):
    start_lat, start_lon = geocoder(start_address)
    time.sleep(1) #prevent going over API limit
    end_lat, end_lon = geocoder(end_address)

    conn = get_db()
    c = conn.cursor()
    c.execute('''
                INSERT INTO routes (start_address, end_address, start_lat, start_lon, end_lat, end_lon, arrival_time, userid)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (start_address, end_address, start_lat, start_lon, end_lat, end_lon, arriveby, userid))
    route_id = c.lastrowid
    conn.commit()
    return getRoute(route_id)


def getRoute(route_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        SELECT routeid, start_address, end_address,
               start_lat, start_lon, end_lat, end_lon,
               arrival_time, userid
        FROM routes
        WHERE routeid = ?
    ''', (route_id,))

    row = c.fetchone()
    if row:
        return Route(*row)
    else:
        return None


def Router(route):
    url = "https://external.transitapp.com/v3/otp/plan"
    headers = {
        "apiKey": TRANSIT_TOKEN
    }
    params = {
        'fromPlace': f"{route.start_lat},{route.start_lon}",
        'toPlace': f"{route.end_lat},{route.end_lon}",
        'arriveBy': 'true',
        'time': route.arrival_time,
        'date': datetime.today()
    }


    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        with open('test_route_response.json', 'w') as f:
            json.dump(data, f, indent=2)
        print("✅ Saved response to test_route_response.json", flush=True)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print("❌ Request Error:", e, flush=True)
        return jsonify({"error": str(e)}), 500


# maybe get route name (if implemented)
# @param userid: user id of requester
# @return tuple: start_address, end_address, arrival_time
def get_saved_routes(userid):
    try:
        with get_db() as db:
            routes = db.execute('''
                SELECT start_address, end_address, arrival_time
                FROM routes
                WHERE userid = ?
                ''', 
                (userid,)).fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
    except Exception as e:
        print(f"Error updating database: {e}")
    finally:
        return routes


def get_all_subway_stops():
    url = "https://external.transitapp.com/v3/public/stops_for_network"
    headers = {
        "apiKey": TRANSIT_TOKEN
    }
    params = {
        'network_id': "NYC Subway|NYC"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        stoplist = response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Request Error:", e, flush=True)
        return jsonify({"error": str(e)}), 500

    try:
        with get_db() as db:
            for stop in stoplist["stops"]:
                db.execute('''  
                    INSERT INTO subway_stops (global_stop_id, parent_station_global_stop_id, route_type, rt_stop_id, stop_lat, stop_lon, stop_name, wheelchair_boarding)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (stop["global_stop_id"], 
                          stop["parent_station_global_stop_id"], 
                          stop["route_type"], 
                          stop["rt_stop_id"], 
                          stop["stop_lat"], 
                          stop["stop_lon"], 
                          stop["stop_name"], 
                          stop["wheelchair_boarding"],))
    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
    except Exception as e:
        print(f"Error updating database: {e}")
