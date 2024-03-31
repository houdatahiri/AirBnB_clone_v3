#!/usr/bin/python3
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from . import states
from . import cities
from . import amenities
from . import users
from . import places
from . import places_reviews
