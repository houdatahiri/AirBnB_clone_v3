#!/usr/bin/python3
"""states"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/states/', methods=['GET'])
def list_states():
    '''Retrieves a list of all State objects'''
    list_states = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    '''Retrieves a State object'''
    all_states = storage.all("State").values()
    stat_object = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if stat_object == []:
        abort(404)
    return jsonify(stat_object[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''Deletes a State object'''
    all_states = storage.all("State").values()
    stat_object = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if stat_object == []:
        abort(404)
    stat_object.remove(stat_object[0])
    for obj in all_states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    '''Creates a State'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def updates_state(state_id):
    '''Updates a State object'''
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    for key, value in data.items():
        ignore_keys = ["id", "created_at", "updated_at"]
        if key not in ignore_keys:
            state.bm_update(key, value)
    state.save()
    state = state.to_json()
    return jsonify(state), 200
