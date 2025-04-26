from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
from dotenv import load_dotenv
import os
# change whenever we change the name of the app
from DailyCommuterBackend.auth import login_required
from DailyCommuterBackend.db import get_db
from DailyCommuterBackend.apiRouting.api import createRoute, Router


load_dotenv()
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
TRANSIT_TOKEN = os.getenv("TRANSIT_TOKEN")


bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    # Update the databases when the home page loads
    # TODO implement updating the db at some interval (maybe every 2 minutes?)
    db = get_db()
    trip_update = db.execute(
        'SELECT *'
        ' FROM trip_update'
        ' WHERE route_id = "GS"'
    ).fetchall()
    for alert in trip_update:
        print(dict(alert))
    return render_template('home/index.html', trip_update = trip_update)


@bp.route('/displayroute/<route_id>')
def map_view(route_id):
    conn = get_db()
    c = conn.cursor()
    query = '''
        SELECT name, lat, lon
        FROM points
        WHERE route_id = ?
        ORDER BY type ASC  -- if you have stop order!
    '''
    c.execute(query, (route_id,))
    rows = c.fetchall()
    conn.close()

    # Structure for the template
    stops = [
        {'name': name, 'lat': lat, 'lon': lon}
        for name, lat, lon in rows
    ]

    return render_template('map.html', stops=stops, MAPBOX_TOKEN = MAPBOX_TOKEN)


@bp.route('/addRoute', methods=['GET', 'POST'])
def createRouteForm():
    if request.method == 'POST':
        start_address = request.form['start_address']
        end_address = request.form['end_address']
        arriveby = request.form['arrival_time']
        userid = '69' #joke user id, to be replaced once users are implemented

        try:
            newroute = createRoute(start_address, end_address, arriveby, userid)
            Router(newroute)
            return redirect(url_for('map_view', route_id=newroute.id)) #should go to saved routes page
        except Exception as e:
            return f"Error: {e}", 500
    return render_template('addroute.html')



