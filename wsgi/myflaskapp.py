import flask_json

app = flask_json.make_json_app(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/ugly')
def uglify():
	return 'Ugly.'


if __name__ == "__main__":
    app.run()

