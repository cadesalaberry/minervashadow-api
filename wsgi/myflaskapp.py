from flask_auth import requires_auth
from flask_json import make_json_app


app = make_json_app(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/transcript')
@requires_auth
def transcript(auth):
	return '{ "hello" : "told ya" }'


@app.route('/auth')
@requires_auth
def auth(auth):
	return auth.username


if __name__ == "__main__":
    app.run()

