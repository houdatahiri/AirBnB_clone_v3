#!/usr/bin/python3
"""
This module contains endpoint(route) status
"""
from flask import Flask
from api.v1.views import app_views
from flask import jsonify
app = Flask(__name__)


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Returns a JSON status
    """
    return jsonify({"status": "OK"})
