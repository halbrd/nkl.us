from flask import Flask, render_template

from tttmaps.views import tttmaps

app = Flask(__name__)

app.register_blueprint(tttmaps, url_prefix='/tttmaps')

@app.route('/')
def index():
	return 'Yep, Flask is working.'

if __name__ == '__main__':
	# as-is, the app will run in debug mode
	# when wsgi runs it, it will be in production mode
	app.run(host='0.0.0.0', debug=True)
