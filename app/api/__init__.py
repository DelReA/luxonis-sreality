from flask import Blueprint

from .flats import api as flats_api


api = Blueprint('api', __name__)
api.register_blueprint(flats_api, url_prefix='/flats')
