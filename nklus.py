from flask import Flask, render_template

from tttmaps.views import tttmaps
from music.views import music

app = Flask(__name__)

app.register_blueprint(tttmaps, url_prefix='/tttmaps')
app.register_blueprint(music, url_prefix='/music')

@app.route('/')
def index():
	return render_template('nklus.html')

if __name__ == '__main__':
	# as-is, the app will run in debug mode
	# when wsgi runs it, it will be in production mode
	app.run(host='0.0.0.0', debug=True)
