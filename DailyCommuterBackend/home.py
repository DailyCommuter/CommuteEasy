from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask_cors import CORS
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
CORS(bp, resources={r"/*": {"origins": "http://localhost:5173"}})


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


@bp.route('/displayroute/<routeid>')
def map_view(routeid):
    conn = get_db()
    c = conn.cursor()
    query = '''
        SELECT name, lat, lon, type
        FROM points
        WHERE routeid = ?
        ORDER BY type ASC
    '''
    c.execute(query, (routeid,))
    rows = c.fetchall()
    conn.close()

    # Structure for the template
    stops = [
        {'name': name, 'lat': lat, 'lon': lon, 'type': type}
        for name, lat, lon, type in rows
    ]
    return render_template('home/map.html', stops=stops, MAPBOX_TOKEN = MAPBOX_TOKEN)


@bp.route('/addRoute', methods=['GET', 'POST'])
def createRouteForm():
    if request.method == 'POST':
        data = request.get_json()
        start_address = data['start_address']
        end_address = data['end_address']
        arriveby = data['arriveby']
        userid = '69'  # placeholder user ID

        try:
            print("before route created")
            print(start_address, end_address, arriveby, userid)
            newroute = createRoute(start_address, end_address, arriveby, userid)
            print("route created")
            Router(newroute)
            return jsonify({"redirect_url": url_for('home.map_view', routeid=newroute.id)}), 200
        except Exception as e:
            return f"Error: {e}", 502
    return render_template('addroute.html')



