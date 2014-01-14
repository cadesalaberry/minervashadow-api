from flask_auth import requires_auth
from flask_json import make_json_app
from flask import jsonify

app = make_json_app(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/transcript')
@requires_auth
def transcript(auth):
	hello = 'told ya'
	return jsonify(hello)


@app.route('/auth')
@requires_auth
def auth(auth):
	return auth.username


if __name__ == "__main__":
    app.run()

