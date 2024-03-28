#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """ Returns a Json response indicating the status """
    return jsonify({"status": "OK"})
