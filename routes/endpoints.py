from flask import Blueprint
from controllers.controllers import *

rg_app = Blueprint('rg_app', __name__)

rg_app.route('/create_image')(create_random_image)