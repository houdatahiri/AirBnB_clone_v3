from flask import Flask
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Function to be called when the application context is torn down.
    It closes the storage connection.

    Args:
        exception: The exception that caused the teardown, if any.
    """
    storage.close()


if __name__ == "__main__":

    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
