from flask import Blueprint, render_template, url_for

import requests

tedcruz = Blueprint('tedcruz', __name__,
					template_folder='templates',
					static_folder='static')

@tedcruz.route('/')
def index():
	#print(requests.get('https://api.twitter.com/1.1/search/tweets.json?q=from%3Acommentiquette%20%40tedcruz&src=typd&lang=en'))

	return render_template('tedcruz.html')
