#!/usr/bin/python3
""" Flask api configuration module. """

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
# import blueprint


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ Function to clear the storage session. """
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """ Customises 404 error message. """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', '5000')),
            threaded=True)
