#!/usr/bin/python3
""" Amenity module """

from api.v1.views import app_views
from models.amenity import Amenity
from flask import abort, jsonify
from models import storage


@app_views.route('/amenities', strict_slashes=False)
def all_amenities():
    """ Retrieves a list of all amenity objects """
    amenities = []
    for amenity in storage.all(Amenity).values():
        amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
def one_amenity(amenity_id):
    """ Retrieves one object using its id """
    obj = storage.get(Amenity, amenity_id)
    if 
