import time
import uuid
from database import db
from app import bcrypt
from user.model.user import User
from utils.utils import *
from response.api_response import APIResponse
def authenticate(login_request: dict):
    if(login_request is None):
        return {
            "message": "Request can't null",
            "status": 404
        }
    user : User = User.query.filter_by(email=login_request['username']).first();
    if(user and bcrypt.check_password_hash(user.password, login_request['password'])):
        auth_response = {
            'token': str(uuid.uuid4()),
            'expiredTime': int(round(time.time() * 1000)) + expired_time,
            'info': {
                'fullName': user.first_name + " " + user.last_name,
                'id': user.id
            }
        }
        auth_response_cache[auth_response['token']] = auth_response
        return auth_response
    return APIResponse(
        "Username or password not match",
        400,
        1,
        None
    ).to_dict()
def register(register_request):
    if (register_request is None):
        APIResponse(
            "Request can't null",
            400,
            1,
            None
        ).to_dict()
    user = User(
        register_request['email'],
        bcrypt.generate_password_hash(register_request['password']).decode('utf-8'),
        register_request['firstName'],
        register_request['lastName']
    )
    db.session.add(user)
    db.session.commit()
    return APIResponse(
        "Created account successfully",
        200,
        0,
        None
    ).to_dict()

