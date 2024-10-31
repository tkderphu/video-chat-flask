from datetime import datetime

from database import db
from user.model.user import User


class Conversation(db.Model):
    __tablename__ = 'conversations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=True)
    conversation_type=db.Column(db.String(150), default='PRIVATE')
    participants = db.relationship('Participation', backref='conversation', lazy=True)
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        users = []
        for participation in self.participants:
            if participation.conversation_id == self.id:
                users.append(participation.user)

        if self.conversation_type=='PRIVATE':
            display_name = 'NONE'
        else:
            display_name = self.name

        messages = Message.query.filter_by(conversation_id=self.id).all();
        return {
            "id": self.id,
            'displayName': display_name,
            'imageRepresent': None,
            'status': True,
            'scope': self.conversation_type,
            'recentMessage': messages[len(messages)-1].to_dict()
        }
class Message(db.Model):
    __tablename__ = 'messages'
    id=db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    message_type = db.Column(db.String(150))
    from_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    conversation_id = db.Column(db.Integer, db.ForeignKey("conversations.id"), nullable=False)
    created_date =db.Column(db.DateTime, default=datetime.now())
    def __init__(self, content, message_type, from_user_id, conversation_id):
        self.content = content
        self.message_type = message_type
        self.from_user_id = from_user_id
        self.conversation_id = conversation_id

    def to_dict(self):
        user : User = User.query.filter_by(id=self.from_user_id).first()
        conversation : Conversation = Conversation.query.filter_by(id=self.conversation_id).first()
        return {
            'id': self.id,
            'content': self.content,
            'messageType': self.message_type,
            'fromUser': user.to_dict(),
            'toConversation': conversation.to_dict(),
            'createdDate': '',
        }

class Participation(db.Model):
    __tablename__ = 'participations'
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    conversation_id=db.Column(db.Integer, db.ForeignKey("conversations.id"), nullable=False)