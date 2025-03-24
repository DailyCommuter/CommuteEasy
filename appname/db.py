import sqlite3
from datetime import datetime
from google.transit import gtfs_realtime_pb2
import click
from flask import current_app, g

import requests

def update_ACE():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get("https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace")
    feed.ParseFromString(response.content)
    i = 0
    while i < 20:
        for entity in feed.entity:
            print(entity)
            i += 1
        #if entity.HasField('trip_update'):
           # print(entity.trip_update) #this will contain a call instead to save this to our db

def update_service():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get("https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts")
    feed.ParseFromString(response.content)
    i = 0
    while i < 20:
        for entity in feed.entity:
            print(entity)
            i += 1


# Register close_db and init_db_command with the Application
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

# Initialize the db
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

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