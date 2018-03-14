from flask import Blueprint, render_template, url_for

import os
import re
from PIL import Image

tttmaps = Blueprint('tttmaps', __name__,
					template_folder='templates',
					static_folder='static')

def generate_thumbnail_url(map_name):
	maps_dir = 'tttmaps/static/maps/'
	if os.path.isfile(maps_dir + '%s_thumbnail.jpg' % map_name):
		return url_for('tttmaps.static', filename='maps/%s_thumbnail.jpg' % map_name)

	cache_dir = maps_dir + 'cache/'
	if not os.path.exists(cache_dir):
		os.makedirs(cache_dir)

	if os.path.isfile(cache_dir + '%s_thumbnail.jpg' % map_name):
		return url_for('tttmaps.static', filename='maps/cache/%s_thumbnail.jpg' % map_name)
	else:
		thumbnail = Image.open(maps_dir + '%s_screenshot_1.jpg' % map_name)
		thumbnail = thumbnail.resize((128, 128), Image.ANTIALIAS)
		thumbnail.save(cache_dir + '%s_thumbnail.jpg' % map_name)
		return url_for('tttmaps.static', filename='maps/cache/%s_thumbnail.jpg' % map_name)

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
			screenshot_match = re.fullmatch(map_name + '_screenshot_(\d+)\.jpg', filename)
			if screenshot_match:
				screenshot_index = screenshot_match.group(1)
				screenshots[screenshot_index] = url_for('tttmaps.static', filename='maps/' + filename)
		map_['screenshots'] = [ screenshots[screenshot_index] for screenshot_index in sorted(screenshots.keys()) ]

		if os.path.isfile('tttmaps/static/maps/%s_thumbnail.jpg' % map_name):
			map_['thumbnail'] = url_for('tttmaps.static', filename='maps/%s_thumbnail.jpg' % map_name)
		elif len(screenshots) > 0:
			map_['thumbnail'] = generate_thumbnail_url(map_name)
		else:
			map_['thumbnail'] = url_for('tttmaps.static', filename='thumbnail_default.jpg')

		data.append(map_)

	data.sort(key=lambda map: map['name'])

	return render_template('index.html', data=data)
