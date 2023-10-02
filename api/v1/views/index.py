#!/usr/bin/python3


from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    Returns a JSON response with the status message "OK"
    """
    return jsonify({"status": "OK"})


@app_views.route("/api/v1/stats", methods=["GET"], strict_slashes=False)
def number_objects():
    """
    Returns the number of objects in each class in the storage.

    :return: JSON response containing the number of objects for each class.
    """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {name: storage.count(cls) for name, cls in zip(names, classes)}

    return jsonify(num_objs)
