from flask import Flask, request, jsonify, Blueprint
from cache import cache
auth_bp = Blueprint('authen', __name__, url_prefix="/api/v1/users/auth")

@auth_bp.route('/login', methods=['GET'])
def login():
    loginRequest = request.get_json()
    cache.auth_response_cache['login'] = 'ok'
    return jsonify(cache.auth_response_cache)
@auth_bp.route('/register', methods=['POST'])
def register():
    register_request = request.get_json()

