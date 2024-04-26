#!/usr/bin/python3xx
'''api status'''
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def get_status():
"""Return a JSON response with status OK."""
    return jsonify({"status": "OK"})
