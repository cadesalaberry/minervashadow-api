from wsgi import myflaskapp

application = myflaskapp.app

if __name__ == '__main__':
	application.run(host='0.0.0.0')