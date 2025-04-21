from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from dotenv import load_dotenv

import os
# change whenever we change the name of the app
from DailyCommuter_Backend.auth import login_required
from DailyCommuter_Backend.db import (
  get_db, update_all_feeds
)

load_dotenv()

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    # Update the databases when the home page loads
    # TODO implement updating the db at some interval (maybe every 2 minutes?)
    update_all_feeds()
    db = get_db()
    trip_update = db.execute(
        'SELECT *'
        ' FROM trip_update'
        ' WHERE route_id = "GS"'
    ).fetchall()
    for alert in trip_update:
        print(dict(alert))
    return render_template('home/index.html', trip_update = trip_update)

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
TRANSIT_TOKEN = os.getenv("TRANSIT_TOKEN")

@bp.route('/map/')
def map_view():
    return render_template('home/map.html', MAPBOX_TOKEN = MAPBOX_TOKEN)

@bp.route('/addRoute', methods=['GET', 'POST'])
def createRouteForm():
    if request.method == 'POST':
        start_address = request.form['start_address']
        end_address = request.form['end_address']
        arriveby = request.form['arrival_time']
        userid = '69' #joke user id, to be replaced once users are implemented

        try:
            newroute = createRoute(start_address, end_address, arriveby, userid)
            print(Router(newroute))
            return redirect('/') #should go to saved routes page
        except Exception as e:
            return f"Error: {e}", 500
    return render_template('addroute.html')



