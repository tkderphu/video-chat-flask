
from flask import Flask
from flask_socketio import SocketIO
from user.controller.user import user_bp
from authen.controller.authenController import auth_bp
app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
socketio = SocketIO(app)


if __name__ == '__main__':
    socketio.run(app)

