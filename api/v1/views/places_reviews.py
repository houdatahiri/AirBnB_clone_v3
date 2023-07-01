#!/usr/bin/python3
"""View for Review objects that handles default API actions."""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def search_place_review(place_id):
    """Return a list of reviews link to a place."""
    selected_place = storage.get(Place, place_id)
    if not selected_place:
        abort(404)
    list_of_reviews = []
    for review in selected_place.reviews:
        list_of_reviews.append(review.to_dict())
    return jsonify(list_of_reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_a_review(review_id):
    """Get a review by its id."""
    wanted_review = storage.get(Review, review_id)
    if not wanted_review:
        abort(404)
    return jsonify(wanted_review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Delete a Review object."""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """Create a Review object."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.is_json:
        abort(400, 'Not a JSON')
    data = request.get_json()
    user_id = data.get('user_id')
    text = data.get('text')
    if not user_id:
        abort(400, 'Missing user_id')
    if not text:
        abort(400, 'Missing text')
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    review = Review(place_id=place_id, user_id=user_id, text=text)
    review.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update a Review object."""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.is_json:
        abort(400, 'Not a JSON')
    data = request.get_json()
    ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
