#!/usr/bin/python3
""" Init file """

from api.v1.views.cities import *
from api.v1.views.states import *
from api.v1.views.index import *
from api.v1.views.amenity import *
from api.v1.views.users import *
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
