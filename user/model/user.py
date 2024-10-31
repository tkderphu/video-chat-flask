
from database import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    online = db.Column(db.Boolean, nullable=False, default=False)
    participants = db.relationship('Participation', backref='user', lazy=True)
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


    def to_dict(self):
        return {
            'email': self.email,
            'password': self.password,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'online': self.online
        }