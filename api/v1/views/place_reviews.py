#!/usr/bin/python3
"""Module with the view for Review objects"""
from api.v1.views import app_views
from models.review import Review
from models.place import Place
from models.city import City
from models.user import User
from models import storage
from flask import request, abort
import json


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'],
                 strict_slashes=False)
def reviews(place_id):
    """Return a list of dictionaries of all reviews for a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if request.method == 'GET':
        reviews = []
        for review in place.reviews:
            reviews.append(review.to_dict())
        return json.dumps(reviews, indent=4)
    try:
        data = request.get_json()
    except Exception:
        return 'Not a JSON', 400
    if 'user_id' not in data.keys():
        return 'Missing user_id', 400
    user = storage.get(User, data.get('user_id'))
    if user is None:
        abort(404)
    if 'text' not in data.keys():
        return 'Missing text', 400
    data['place_id'] = place_id
    new_review = Review(**data)
    new_review.save()
    return json.dumps(new_review.to_dict(), indent=4), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_review(review_id):
    """Get a review instance from the storage"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if request.method == 'GET':
        return json.dumps(review.to_dict(), indent=4)
    if request.method == 'DELETE':
        review.delete()
        storage.save()
        return {}
    if request.method == 'PUT':
        try:
            data = request.get_json()
        except Exception:
            return 'Not a JSON', 400
        for k, v in data.items():
            if k != 'id' or k != 'user_id' or k != 'place_id'\
               or k != 'created_at' or k != 'updated_at':
                setattr(review, k, v)
        storage.save()
        return json.dumps(review.to_dict(), indent=4), 200
