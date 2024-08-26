from flask import Blueprint, request, Response, jsonify

import config

mod = Blueprint('list_route', __name__)

@mod.route('/api/<resource_name>', methods=['GET'])
def list_route(resource_name):
    body = request.get_json()
    
    sort = body.get('sort', None)
    filter = body.get('filter', None)
    pagination = body.get('pagination', None)