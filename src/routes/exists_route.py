from flask import Blueprint, request, Response, jsonify

import config

mod = Blueprint('exists_route', __name__)

@mod.route('/api/<resource_name>/<id>', methods=['HEAD'])
def exists_route(resource_name, id):
    pass