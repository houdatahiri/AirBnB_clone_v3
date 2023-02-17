#!/usr/bin/python3
'''index view for API'''
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns JSON """
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat():
    '''Number of each object by type'''
    return jsonify(
            amenities=storage.count(Amenity),
            cities=storage.count(City),
            places=storage.count(Place),
            reviews=storage.count(Reviews),
            states=storage.count(State),
            users=storage.count(User)
        )
