#!/usr/bin/python3
""" Amenity module """

from api.v1.views import app_views
from models.user import User
from flask import abort, jsonify, make_response, request
from models import storage


@app_views.route('/users', strict_slashes=False)
def all_users():
    """ Retrieves a list of all User objects """
    users = []
    for obj in storage.all(User).values():
        users.append(obj.to_dict())
    return make_response(jsonify(users), 200)


@app_views.route('/users/<user_id>', strict_slashes=False)
def one_user(amenity_id):
    """ Retrieves one object using its id """
    obj = storage.get(Amenity, amenity_id)
    if obj:
        return make_response(jsonify(obj.to_dict()), 200)
    abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_amenity(amenity_id):
    """ Deletes an Amenity obj """
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        amenity.delete()
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    """ Creates a new Amenity object """
    if request.is_json is True:
        data = request.get_json()
        if 'name' in data.keys():
            obj = Amenity(**data)
            storage.new(obj)
            storage.save()
            return make_response(jsonify(obj.to_dict()), 201)
        abort(400, "Missing name")
    abort(400, "Not a JSON")


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """ Updates an existing amenity object """
    if request.is_json is True:
        data = request.get_json()
        obj = storage.get(Amenity, amenity_id)
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(obj, key, value)
        obj.save()
        return make_response(jsonify(obj.to_dict()), 200)
    abort(400, "Not a JSON")
