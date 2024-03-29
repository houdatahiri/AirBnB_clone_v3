#!/usr/bin/python3
"""index file"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


@app_views.route('/status')
def status_1():
    """return status ok and 200 response thx to jsonify"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def status_2():
    """ return number of each object below"""
    return jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
        })
