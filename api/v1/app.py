#!/usr/bin/python3
""" Main app """

from os import getenv
from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app, origins='*')


@app.teardown_appcontext
def close_storage(exc):
    """Close the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """404 page not found"""
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    # set defaults if env variables are not set
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))

    # run the app
    app.run(host=host, port=port, debug=1)
