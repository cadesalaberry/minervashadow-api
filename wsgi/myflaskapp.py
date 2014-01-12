from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/ugly')
def uglyfy():
	return 'Ugly.'


if __name__ == "__main__":
    app.run()

