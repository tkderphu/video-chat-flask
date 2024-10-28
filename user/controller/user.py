
from flask import jsonify, request, Blueprint
from cache import  cache
user_bp = Blueprint('user', __name__, url_prefix='/api/v1/users')

@user_bp.route('',methods=['GET'])
def get_users():
    cache.auth_response_cache['cache'] ='huhu'
    return jsonify(cache.auth_response_cache), 200