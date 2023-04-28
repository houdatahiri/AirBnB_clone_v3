#!/usr/bin/pyhton3
"""Views for States"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.state import State


@app_views.route('/states',
                 method=['GET', 'POST'], strict_slashes=False)
@app_views.route('/states/<states.id>',
                 method=['PUT', 'DELETE'], strict_slashes=False)
def state_object(state_id=None):
    """ A Function that performs CRUD for State Class"""

	my_states = storage.all(States)

	states = [obj.to_dict() for items in my_states.values()]
	if not state_id:
	    if request.method == 'GET':
		    for state in states:
	    if request.method == 'GET';
			return jsonify(states)
		elif request.method == 'POST':
			my_dict = request.get_json()

			if my_dict is None:
				abort(400, 'Not a JSON')
			if my_dict.get("name") is None:
				abort(400, 'Missing Name')
			new_state = State(**my_dict)
			new_state.save()
			return jsonify(new_state.to_dict())

	else:
		if request.method == 'GET':
        	for state in states:
            	if state.get('id') == state_id:
             		return jsonify(state)
        	abort(404)
        
		elif request.method == 'PUT':
		    my_dict =request.get_json()

			if my_dict is None:
			    abort(400,'Not a JSON')
			for state in my_states.values()
				if state.id == state_id:
				   state.name = my_dict.get('name')
				   state.save()
				   return jsonify(state.to_dict()), 200
			abort(404)

		elif request.method == 'PUT':


