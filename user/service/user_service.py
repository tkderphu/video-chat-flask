
from ..model.user import User

def get_users():
    users = []
    for user in User.query.all():
        users.append(user.to_dict())
    return users;