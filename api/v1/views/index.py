#!/usr/bin/python3
"""This script starts the Flask web application"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Get the number of each object type"""
    stats = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
    }
    return jsonify(stats)
