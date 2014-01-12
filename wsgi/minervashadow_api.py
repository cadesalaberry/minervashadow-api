from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/ugly')
def uglyfy():
	return 'Ugly.'


@app.route('/pretty')
def uglyfy():
	return 'Pretty.'


if __name__ == '__main__':
    app.run()

