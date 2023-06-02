from flask import Blueprint, jsonify

from app.models import Flat as FlatModel

api = Blueprint('flats', __name__)


@api.route('/', methods=['GET'])
def get_all_flats():
  return jsonify([flat.raw for flat in FlatModel.get_all_flats()])
