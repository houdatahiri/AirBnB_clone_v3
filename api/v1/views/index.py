#!/usr/bin/python3xx
'''api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views

class_objects = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }

@app_views.route('/status', methods=['GET'])
def status():
    '''method that routes to status pageand returns the status'''
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def stats():
    '''method that returns the number of each objects by type'''
    num_of_obj_type = {}
    for key in class_objects:
        num_of_obj_type[key] = storage.count(class_objects[key])
    return jsonify(num_of_obj_type)
