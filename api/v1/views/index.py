#!/usr/bin/py
"""
"""
from Flask import Flask
from api.v1.views import app_views
app = flask(__name__)
app.route('/status')
def status():
    """ """
    return 'test'
