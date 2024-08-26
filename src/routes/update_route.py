from flask import Blueprint, request, Response, jsonify

import config

mod = Blueprint('update_route', __name__)

@mod.route('/api/<resource_name>/<id>', methods=['PUT'])
def update_route(resource_name, id):
    data = request.get_json()