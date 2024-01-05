#!/usr/bin/python3
"""view index"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from collections import OrderedDict

class_plurals = {'amenities': Amenity, 'cities': City, 'places': Place,
                 'reviews': Review, 'states': State, 'users': User}


@app_views.route('/status', strict_slashes=False)
def status():
    """the state of the v1 API"""
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Itemized count of the objects stored in each class.

    """
    stats = OrderedDict()
    for key in sorted(class_plurals.keys()):
        count = storage.count(class_plurals[key])
        if count > 0:
            stats[key] = count
    return jsonify(stats)
