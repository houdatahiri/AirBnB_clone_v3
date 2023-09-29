#!/usr/bin/python3
"""API calls handled here"""
from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views
from api.v1.views import app_views
import os


app = Flask(__name__)
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Terminates the database connection after handling the request"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors
       Returns a json formatted error message."""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
