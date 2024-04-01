#!/usr/bin/python3
"""API blueprint initialization"""

from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Wildcard import of everything in the package api.v1.views.index
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
