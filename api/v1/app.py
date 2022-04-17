#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# app_views BluePrint defined in api.v1.views
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    """
    Main Flask app
    """
    # start Flask app
    app.run(host=host, port=port, threaded=True)
