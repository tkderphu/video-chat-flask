from flask import request, jsonify, Blueprint
auth_bp = Blueprint('authen', __name__, url_prefix="/api/v1/users/auth")
from ..service import authen_service

@auth_bp.route('/login', methods=['GET'])
def login():
    loginRequest = request.get_json()
    return jsonify(authen_service.authenticate(loginRequest))
@auth_bp.route('/register', methods=['GET'])
def register():
    register_request = request.get_json();
    return jsonify(authen_service.register(register_request))

