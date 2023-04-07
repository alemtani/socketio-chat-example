from app import socketio
from flask import Blueprint, jsonify
from flask_socketio import emit

sockets = Blueprint('sockets', __name__)

@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)