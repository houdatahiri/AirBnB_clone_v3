#!/usr/bin/python3
"""
create Flask app, app_views
"""

from flask import jsonify, make_response, current_app
from api.v1.views import app_views
from models import storage


@app_views.route("/status")
def api_status():
    """returns status Ok if working"""
    response = make_response(jsonify({'status': "OK"}), 200)
    return (response)


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def get_stats():
    """returns the stats of the api"""
    stats = {}
    # stats = {
    #         "amenities": storage.count('Amenity'),
    #         "cities": storage.count('City'),
    #         "places": storage.count('Place'),
    #         "reviews": storage.count("Review"),
    #         "states": storage.count("State"),
    #         "users": storage.count("User")
    #         }
    obj_types = {
        'Amenity': "amenities",
        'City': "cities",
        'Place': "places",
        'Review': "reviews",
        'State': "states",
        'User': "users"
        }

    # for obj in obj_types.keys():
    #     if storage.count(obj):
    #         stats[obj_types[obj]] = storage.count(obj)

    return jsonify(stats)
