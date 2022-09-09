#!/usr/bin/python3
"""
file __init__.py
"""
from flask import Blueprint
app_views = Blueprint('api', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *
