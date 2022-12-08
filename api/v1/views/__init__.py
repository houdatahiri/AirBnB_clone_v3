from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

"""Import for flask app"""
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *


