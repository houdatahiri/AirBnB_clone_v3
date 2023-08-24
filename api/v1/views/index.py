#!/usr/bin/python3
"""endpoint"""

from models import storage
from api.v1.app import app_views
from flask import jsonify

@app_views.route("/status")
def status():
    """api status"""
    return jsonify({"status": "OK"})

@app_views.route("/api/v1/stats")
def objects():
    """retrice"""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
  