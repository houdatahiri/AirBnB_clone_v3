#!/usr/bin/python3
""" something for now"""

from flask import Flask, Blueprint, render_template
from models import storage
from api.v1.views import app_view
from os import getenv



app = Flask(__name__)
app.register_bluprint(app_view)

@app.teardown_appcontext
def teardown_appcontext():
    storage.close()

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = "0.0.0.0"
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
