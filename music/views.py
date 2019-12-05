from flask import Blueprint

music = Blueprint('music', __name__,
                  template_folder='templates',
                  static_folder='static')

@music.route('/')
def index():
    return 'yes this is music'
