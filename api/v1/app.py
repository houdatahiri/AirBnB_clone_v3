#!/usr/bin/python3
"""The app engine for the flask app"""

from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear(_):
    """ Closes the storage """
    storage.close()

if __name__ == '__main__':
    host = getenv('HBNB_API_HOST') if getenv('HBNB_API_HOST') else '0.0.0.0'
    port = getenv('HBNB_API_PORT') if getenv('HBNB_API_PORT') else 5000
    app.run(host=host, port=int(port), threaded=True)
