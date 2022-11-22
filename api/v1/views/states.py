#!/usr/bin/python3
""" view for State objects that handles all default RESTFul API actions """
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ Retrieve all state objects """
    list_obj = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(list_obj)


@app_views.route('/states/<state_id>', methods=['GET'])
def getId(state_id):
    """ Retrieves a State object by id """
    obj = storage.get("State", state_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def deleteId(state_id):
    """ Delete state object by id """
    obj = storage.get("State", state_id)
    if obj is None:
        abort(404)
    obj.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def newState():
    """ Returns the new State """
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    new = request.get_json()
    obj = State(**new)
    obj.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update(state_id):
    """ Update the State object """
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    obj = storage.get("State", state_id)
    if obj is None:
        abort(404)
    for k, v in request.get_json().items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(obj, k, v)
    storage.save()
    return jsonify(obj.to_dict())
