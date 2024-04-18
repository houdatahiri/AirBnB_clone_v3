#!/usr/bin/python3
"""import thing here to avoid circular import"""
from flask import Blueprint


app_views = Blueprint('/api/v1', __name__, url_prefix="/api/v1")

from api.v1.views.users import *
