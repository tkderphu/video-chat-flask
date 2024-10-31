# app.py
from flask import Flask
from flask_socketio import SocketIO
from database import db  # Import db from database.py
from user.controller.user import user_bp
from authen.controller.authen_controler import auth_bp
from flask_bcrypt import Bcrypt
from user.model.user import User
from messenger.model.model import Conversation
from messenger.model.model import Message
from messenger.model.model import Participation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:irohas2004@localhost/video_chat_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app context
db.init_app(app)
socketio = SocketIO(app)
bcrypt = Bcrypt(app)
# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)



# Ensure tables are created
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    socketio.run(app)
