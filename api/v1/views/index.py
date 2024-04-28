from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """
    Retrieves the status of the API.

    Returns:
        A JSON response containing the status of the API.
    """
    return jsonify({'status': 'OK'})
