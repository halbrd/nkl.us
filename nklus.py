from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Yep, Flask is working.'

@app.route('/tttmaps/<name>')
def tttmaps(name):
	return render_template('tttmaps.html', name=name)

if __name__ == '__main__':
	# as-is, the app will run in debug mode
	# when wsgi runs it, it will be in production mode
	app.run(host='0.0.0.0', debug=True)

