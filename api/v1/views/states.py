#!/usr/bin/python3
"""View for State objects that handles all default RestFul API"""
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, abort, request, make_response


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Returns a json object with all the states"""
    list_dict = []
    for obj in storage.all(State).values():
        list_dict.append(obj.to_dict())
    return jsonify(list_dict), 200


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """Returns a json object with the state with given id"""
    obj = storage.get(State, state_id)
    if (obj):
        return jsonify(obj.to_dict()), 200
    else:
        abort(404)


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Delete a state"""
    obj = storage.get(State, state_id)
    if (obj):
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Create a new state"""
    conten = request.get_json()
    if conten is None:
        return "Not a JSON", 400
    if conten.get('name') is None:
        return "Missing name", 400
    else:
        new_obj = State(**conten)
        storage.new(new_obj)
        storage.save()
    return jsonify(new_obj.to_dict()), 201


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def update_state(state_id):
    """Update a state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(state, attr, val)
    storage.save()
    return jsonify(state.to_dict())
