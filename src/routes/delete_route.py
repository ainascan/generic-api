from flask import Blueprint, request, Response, jsonify

import config

mod = Blueprint('delete_route', __name__)

@mod.route('/api/<resource_name>/<id>', methods=['DELETE'])
def delete_route(resource_name, id):
    pass