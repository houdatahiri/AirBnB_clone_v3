#!/usr/bin/python3
"""App module using Flask"""
from flask import Flask, jsonify, Response
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
        closes storage
    """
    storage.close()


if __name__ == '__main__':
    """
        main function
    """
    app.run(host=os.getenv('HBNB_API_HOTS', '0.0.0.0'),
            port=os.getenv('HBNH_API_PORT', '5000'),
            threaded=True, debug=False)
