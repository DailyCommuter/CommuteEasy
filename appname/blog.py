from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# change whenever we change the name of the app
from appname.auth import login_required
from appname.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    # Make a variable for retrieving the data from the db
    # Something like this:
    subway_routes = db.execute(
        'SELECT s.id, title, body, created, author_id, username'
        ' FROM post s JOIN user u ON s.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', subway_routes=subway_routes)