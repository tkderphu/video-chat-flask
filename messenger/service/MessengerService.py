
from database import  db
from ..model.model import  Conversation
from ..model.model import  Message
from ..model.model import  Participation
from utils import utils
def create_message(message_request):
    conversation = Conversation.query.filter_by(id=message_request['destId']).first()
    # content, message_type, from_user_id, conversation_id
    if conversation is None:
        conversation = Conversation()
        db.session.add(conversation)
        participation = Participation(
            user_id=message_request['destId'],
            conversation_id=conversation.id
        )
        db.session.add(participation)
        participation = Participation(
            user_id=utils.user_login.get('id'),
            conversation_id=conversation.id
        )
        db.session.add(participation)

    if message_request['video'] is True:
        type = 'VIDEO'
    else:
        type = 'TEXT'
    message = Message(
        message_request['content'],
        type,
        utils.user_login['id'],
        conversation.id
    )
    db.session.add(message)
    db.session.commit()
def create_conversation(conversation_request):
    conversation = Conversation(
        conversation_request['name'],
        'PUBLIC'
    )
    db.session.add(conversation)
    for userId in conversation_request['userIds']:
        participation = Participation(
            user_id=userId,
           conversation_id= conversation.id
        )
        db.session.add(participation)
    db.session.commit()
    return conversation.to_dict()

def get_all_conversation_of_current_user():
    conversations = []