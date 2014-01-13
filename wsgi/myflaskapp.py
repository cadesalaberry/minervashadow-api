from flask_auth import requires_auth
from flask_json import make_json_app


app = make_json_app(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/ugly')
@requires_auth
def uglify():
	return 'Ugly.'


@app.route('/transcript')
@requires_auth
def transcript(auth):
	return '{ "hello" : "told ya" }'


@app.route('/auth')
@requires_auth
def auth(auth):
	return str(auth)


if __name__ == "__main__":
    app.run()

