from flask import Blueprint, render_template, url_for

import requests
import json
import twitter

tedcruz = Blueprint('tedcruz', __name__,
					template_folder='templates',
					static_folder='static')

auth = json.load(open('tedcruz/config.json', 'r'))

api = twitter.Api(consumer_key=auth['consumer_key'], consumer_secret=auth['consumer_secret'], access_token_key=auth['access_token_key'], access_token_secret=auth['access_token_secret'])

@tedcruz.route('/')
def index():
	tweets = api.GetSearch(raw_query='l=&q=from%3Acommentiquette%20%40tedcruz&src=typd')

	return render_template('tedcruz.html', data=tweets)
