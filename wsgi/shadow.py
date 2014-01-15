
from minervashadow import minerva
from functools import wraps
from flask import request

import json


def login_ok(username, password):

	credentials = [username, password]
	_shadow = minerva.MinervaSession(credentials)

	if 'Welcome' in _shadow.login():
		return True
	return False


def get_transcript():

	_cred = request.authorization

	_credentials = [_cred.username, _cred.password]
	_shadow = minerva.MinervaSession(_credentials)
	_shadow.login()

	_curriculum = _shadow.transcript()
	_json = _curriculum.json()

	return json.loads(_json)
	