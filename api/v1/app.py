#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


def launch():
    """App Launcher"""
    # Retrieve host and port from environment variables
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=int(port), threaded=True)


if __name__ == "__main__":
    launch()
