#!/usr/bin/python3
"""
View for City objects that handles
ll default RESTFul API actions
"""

from flask import jsonify, abort, request, make_response
from models.state import State
from models import storage
from api.v1.views import app_views
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=["GET"],
                 strict_slashes=False)
def get_cities(state_id):
    """Gets a list of cities"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    return jsonify([city.to_dict() for city in state.cities])


@app_views.route("/cities/<city_id>", methods=["GET"],
                 strict_slashes=False)
def get_city(city_id):
    """Gets city object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_city(city_id):
    """Deletes a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    # storage.delete(city)
    city.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route("/states/<state_id>/cities", methods=["POST"],
                 strict_slashes=False)
def create_city(state_id):
    """creates a city"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    city_data = request.get_json()

    if not city_data:
        abort(400, "Not a JSON")

    if "name" not in city_data:
        abort(400, "Missing name")

    new_city = City(**city_data)
    setattr(new_city, "state_id", state_id)
    storage.new(new_city)
    storage.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route("/cities/<city_id>", methods=["PUT"],
                 strict_slashes=False)
def update_city(city_id):
    """Updates a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data_to_update = request.get_json()
    if not data_to_update:
        abort(400, "Not a JSON")
    for key, value in data_to_update.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
