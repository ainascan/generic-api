from flask import Blueprint, request, Response, jsonify

import config

mod = Blueprint('create_route', __name__)

@mod.route('/api/<resource_name>', methods=['POST'])
def create_route(resource_name):
    data = request.get_json()