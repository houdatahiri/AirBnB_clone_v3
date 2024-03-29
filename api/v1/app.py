#!/usr/bin/python3
"""Flask app Module"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(error):
    """close storage"""
    storage.close()


if __name__ == '__main__':
    HBNB_API_HOST = getenv("HBNB_API_HOST")\
        if getenv("HBNB_API_HOST") else "0.0.0.0"
    HBNB_API_PORT = int(getenv("HBNB_API_PORT"))\
        if getenv("HBNB_API_PORT") else 5000

    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True, debug=True)
