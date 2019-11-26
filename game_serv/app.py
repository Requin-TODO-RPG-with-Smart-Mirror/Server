from flask import Flask
from flask_socketio import SocketIO, emit
from mongoengine import *

from const import _MONGO_SETTING
from models.mirror import MirrorModel


app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins="*", async_mode="threading")
connect(**_MONGO_SETTING)


@socket.on('register')
def register(data):
    mirror = MirrorModel.objects(mirror_key=data['key']).first()
    emit('register_char', {
        'mirror_key': mirror['mirror_key'],
        'name': mirror['name'],
        'exp': 0
    }, broadcast=True)


@socket.on('show_todo')
def todo(data):
    mirror = MirrorModel.objects(name=data['mirror_key']).first()
    emit('get_todo', {
        'mirror_key': mirror['key'],
        'exp': 0,
        'todo': mirror['todo']
    }, broadcast=True)


@socket.on('now_look')
def look(data):
    mirror = MirrorModel.objects(mirror_key=data['key']).first()
    print('LOOK')
    emit('get_look', {
        'mirror_key': mirror['mirror_key'],
        'head': mirror['character']['head'],
        'body': mirror['character']['body'],
        'exp': 0,
        'todo': mirror['todo']
    }, broadcast=True)



if __name__ == '__main__':
    socket.run(app, host='0.0.0.0', port=5556)