import flask
from functools import wraps
import json

from flask import session, jsonify


def requires_auth(role=None):
	def wrapper(f):
		@wraps(f)
		def decorated(*args, **kwargs):
			if 'user_id' not in session:
				return jsonify(msg='Unauthorized Request!'), 401

			user_privileges = json.loads(session.get('user_privilege', '[]'))
			user_role = session.get('role')

			if role is not None:
				if isinstance(role, list):
					if not any(each in user_privileges for each in role):
						return jsonify(msg='Unauthorized Request!'), 401
				elif role not in user_role:
					return jsonify(msg='Unauthorized Request!'), 401

			return f(*args, **kwargs)

		return decorated

	return wrapper


def store_session(user):
	"""
	Stores user data in Flask session after login.

	:param user: Dictionary containing user data (id, email, role, privileges).
	"""
	session['user'] = user['user']
	session['token'] = user['token']

	return True
