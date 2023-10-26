#!/usr/bin/python3
"""app.py"""
from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def tear(self):
    """Teardown method that closes the storage"""
    storage.close()


@app.errorhandler(404)
def error(e):
    """error handler that returns 404 in just json"""
    json_text = {"error": "Not found"}
    return jsonify(json_text), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
