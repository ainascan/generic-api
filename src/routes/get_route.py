from flask import Blueprint, request, Response, jsonify

import config

mod = Blueprint('get_route', __name__)

@mod.route('/api/<resource_name>/<id>', methods=['GET'])
def get_route(resource_name, id):
    pass