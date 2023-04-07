from config import Config
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

cors = CORS()
socketio = SocketIO(cors_allowed_origins='http://localhost:3000')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)
    socketio.init_app(app)

    from app.sockets import sockets
    app.register_blueprint(sockets)

    return app