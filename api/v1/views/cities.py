#!/usr/bin/python3
''''''
from flask import jsonify, request, make_response, abort
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    state = storage.get(State, state_id)
    cities_list = []
    for elem in state.cities:
        cities_list.append(elem.to_dict())
    return jsonify(cities_list)

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    if not storage.get(State, state_id):
        abort(404)
    if not request.get_json():
        abort(400, description='Not a JSON')
    if 'name' not in request.get_json():
        abort(400, description='Missing name')
    query = request.get_json()
    query['state_id'] = state_id
    new = City(**query)
    new.save()
    return make_response(jsonify(new.to_dict()), 201)

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    return make_response(jsonify({}), 200)

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    if not storage.get(City, state_id):
        abort(404)
    if request.content_type != 'application/json':
        abort(400, description='Not a JSON')
    city = storage.get(City, city_id)
    query = request.get_json()
    ignore_list = ['id', 'state_id', 'created_at', 'updated_at']
    for key, val in query.items():
        if key not in ignore_list:
            setattr(city, key, val)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
        
