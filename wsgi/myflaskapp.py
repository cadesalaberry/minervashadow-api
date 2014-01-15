from flask.ext.httpauth import HTTPBasicAuth
from flask import jsonify, request

import flask_json
import shadow


app = flask_json.make_json_app(__name__)
auth = HTTPBasicAuth()


@app.route('/')
def index():
	return app.send_static_file('index.html')


@app.route('/logout')
@auth.login_required
def logout():
	return jsonify(message='Logged out?')


@app.route('/transcript')
@auth.login_required
def transcript():
	
	return jsonify(shadow.get_transcript())


@app.route('/cookie')
@auth.login_required
def cookie():
	_cred = request.authorization
	return jsonify(username=_cred.username)


@auth.verify_password
def verify_password(username, password):
	"""
	This functiontries to login to check if a username /
	password combination is valid.
	"""
	return shadow.login_ok(username, password)


if __name__ == "__main__":
	app.run()

