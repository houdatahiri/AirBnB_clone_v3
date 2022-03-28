#!/usr/bin/python3
""" API view for State objects. """
import os
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET'])
def all_states(text="is-cool"):
    """ Returns list of all State objs. """
    all_states = storage.all(State)
    list_all_states = []
    for state in all_states:
        list_all_states.append(all_states[state].to_dict())
    return jsonify(list_all_states)

@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """ Returns the State obj in JSON. """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state["State.{}".format(state_id)].to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ Deletes the State obj from storage. """
    deleted = {}
    storage.delete(storage.get(State, state_id)["State.{}".format(state_id)])
    return jsonify(deleted), 200

@app_views.route('/states', methods=['POST'])
def create_state(text="is_cool"):
    """ Creates a new State obj. """
    if not request.json or not 'name' in request.json:
        abort(404)
    content = request.get_json()

    new_state = State(**content)
    new_state.save()
    return jsonify(new_state.to_dict())
