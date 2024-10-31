


auth_response_cache = {

}

expired_time = 86400000

user_login = {
    'id': None,
    'fullName': None
}

def set_context_user_login(request):
    return request.headers.get('your-header-name')
