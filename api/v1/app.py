#!/usr/bin/python3
"""Start server"""

from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(error):
    """Close db session"""
    storage.close()


@app.errorhandler(404)
def error_handler_404(error):
    """404 error"""
    return make_response(jsonify({"error": "Not found"}))


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
