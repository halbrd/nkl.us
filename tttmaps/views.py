from flask import Blueprint, render_template, url_for

import os
import re
from PIL import Image

tttmaps = Blueprint('tttmaps', __name__,
					template_folder='templates',
					static_folder='static')

def generate_thumbnail_url(map_name):
	if os.path.isfile('tttmaps/static/maps/%s_thumbnail.png' % map_name):
		return url_for('tttmaps.static', filename='maps/%s_thumbnail.png' % map_name)

	if os.path.isfile('tttmaps/static/maps/cache/%s_thumbnail.png' % map_name):
		return url_for('tttmaps.static', filename='maps/cache/%s_thumbnail.png' % map_name)
	else:
		thumbnail = Image.open('tttmaps/static/maps/%s_screenshot_1.png' % map_name)
		thumbnail = thumbnail.resize((128, 128), Image.ANTIALIAS)
		thumbnail.save('tttmaps/static/maps/cache/%s_thumbnail.png' % map_name)
		return url_for('tttmaps.static', filename='maps/cache/%s_thumbnail.png' % map_name)

@tttmaps.route('/')
def index():
	data = []
	for data_filename in filter(lambda filename: filename.endswith('_data.json'), os.listdir('tttmaps/static/maps')):
		map_ = {}

		map_name_length = len(data_filename) - len('_data.json')
		map_name = data_filename[:map_name_length]
		map_['name'] = map_name

		screenshots = {}
		for filename in os.listdir('tttmaps/static/maps'):
			screenshot_match = re.fullmatch(map_name + '_screenshot_(\d+)\.png', filename)
			if screenshot_match:
				screenshot_index = screenshot_match.group(1)
				screenshots[screenshot_index] = url_for('tttmaps.static', filename='maps/' + filename)
		map_['screenshots'] = [ screenshots[screenshot_index] for screenshot_index in sorted(screenshots.keys()) ]

		if os.path.isfile('tttmaps/static/maps/%s_thumbnail.png' % map_name):
			map_['thumbnail'] = url_for('tttmaps.static', filename='maps/%s_thumbnail.png' % map_name)
		elif len(screenshots) > 0:
			map_['thumbnail'] = generate_thumbnail_url(map_name)
		else:
			map_['thumbnail'] = url_for('tttmaps.static', filename='thumbnail_default.png')

		data.append(map_)

	return render_template('index.html', data=data)
