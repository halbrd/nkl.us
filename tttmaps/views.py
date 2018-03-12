from flask import Blueprint, render_template, url_for

import os

tttmaps = Blueprint('tttmaps', __name__,
					template_folder='templates',
					static_folder='static')

@tttmaps.route('/')
def index():
	data = []
	for filename in filter(lambda filename: filename.endswith('_data.json'), os.listdir('tttmaps/static/maps')):
		map_ = {}

		map_name_length = len(filename) - len('_data.json')
		map_name = filename[:map_name_length]
		map_['name'] = map_name

		if os.path.isfile('tttmaps/static/maps/%s_thumbnail.png' % map_name):
			map_['thumbnail'] = url_for('tttmaps.static', filename='maps/%s_thumbnail.png' % map_name)
		else:
			map_['thumbnail'] = url_for('tttmaps.static', filename='thumbnail_default.png')

		data.append(map_)

	return render_template('index.html', data=data)
