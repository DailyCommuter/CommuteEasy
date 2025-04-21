import sqlite3
from datetime import datetime
import click
from flask import current_app, g


'''
Functions for initialization and teardown of the app
'''

# for Gideok
def get_all_subway_stops():
    pass


# Register close_db and init_db_command with the Application
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# Initialize the db
def init_db():
    db = get_db()
    db.execute('pragma foreign_keys=ON')

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
        # Enable foreign key support
        g.db.execute('PRAGMA foreign_keys = ON;')

    return g.db


# Close the db when finished with the request
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()