#!/usr/bin/python3
"""Module containing API routes"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from logging.config import dictConfig

classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route('/status', strict_slashes=False)
def status():
    res = {"status": "OK"}
    return res


@app_views.route('/stats', strict_slashes=False)
def stats():
    counts = {}
    for cls in classes:
        counts.update({cls: storage.count(classes[cls])})
    return jsonify(counts)
