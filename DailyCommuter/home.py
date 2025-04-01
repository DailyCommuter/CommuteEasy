from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# change whenever we change the name of the app
from DailyCommuter.auth import login_required
from DailyCommuter.db import (
  get_db, update_all_feeds
)

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    # Update the databases when the home page loads
    # TODO implement updating the db at some interval (maybe every 2 minutes?)
    update_all_feeds()
    db = get_db()
    subway_alerts = db.execute(
        'SELECT *'
        ' FROM subway_alerts'
        ' WHERE route_id = "GS"'
    ).fetchall()
    for alert in subway_alerts:
        print(dict(alert))
    return render_template('home/index.html', subway_alerts = subway_alerts)