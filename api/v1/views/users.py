#!/usr/bin/python3
""" Your first endpoint (route) will be to return the status of your API """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User
import json

@app_views.route("/users/", methods=['GET', 'POST'])
@app_views.route("/users", methods=['GET', 'POST'])
def show_users():
    """ returns list of states """
    if request.method == 'GET':
        lista = []
        users = storage.all(User).values()
        for user in users:
            lista.append(user.to_dict())
        return jsonify(lista)
    elif request.method == 'POST':
        if request.json:
            new_dict = request.get_json()
            if "email" in new_dict.keys():
                new_user = User(**new_dict)
                storage.new(new_user)
                storage.save()
                return jsonify(new_user.to_dict()), 201
            else:
                abort(400, description="Missing email")
            if "password" in new_dict.keys():
                new_user = User(**new_dict)
                storage.new(new_user)
                storage.save()
                return jsonify(new_user.to_dict()), 201
            else:
                abort(400, description="Missing password")
        else:
            abort(400, description="Not a JSON")

@app_views.route("users/<user_id>/", methods=['GET', 'DELETE', 'PUT'])
@app_views.route("users/<user_id>", methods=['GET', 'DELETE', 'PUT'])
def show_user(user_id):
    """ returns user data """
    if request.method == 'GET':
        users = storage.all(User).values()
        for user in users:
            if user.id == user_id:
                return jsonify(user.to_dict())
        abort(404)
    elif request.method == 'DELETE':
        users = storage.all(User).values()
        for user in users:
            if user.id == user_id:
                user.delete()
                storage.save()
                return jsonify({}), 200
        abort(404)
    elif request.method == 'PUT':
        if request.json:
            new_dict = request.get_json()
            users = storage.all(User).values()
            for user in users:
                if user.id == user_id:
                    user.email = new_dict['email']
                    user.password = new_dict['password']
                    storage.save()
                    return jsonify(user.to_dict()), 200
            abort(404)
        else:
            abort(400, description="Not a JSON")
