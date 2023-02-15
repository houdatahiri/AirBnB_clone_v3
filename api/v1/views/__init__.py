#!/usr/bin/python3
"""
initializes the Blueprint app_views and imports the module views.index.
"""

from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
