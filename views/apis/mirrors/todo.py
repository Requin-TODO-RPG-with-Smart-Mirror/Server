import socketio

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.mirror import MirrorModel


api = Api(Blueprint(__name__, __name__))
api.prefix = '/todo'

@api.resource('/register')
class RegisterTodoManagement(Resource):
    @jwt_required
    def get(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()

        return {
            'todo':mirror['todo']
        }

    @jwt_required
    def post(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()
        todo_name: str = request.json['todo_name']
        todo_time: int = request.json['time']
        todo_important: int = request.json['important']

        if not ( todo_important > 0 and todo_important <= 3 ):
            abort(403)

        mirror.todo.append(
            {
                'name':todo_name,
                'time':todo_time,
                'important':todo_important,
                'check': False
            }
        )

        mirror.save()

        sio = socketio.Client()
        sio.connect('http://{}:{}'.format('127.0.0.1', 5556))
        sio.emit('show_todo', {
            'key': get_jwt_identity()
        })

        return {
            'status':'OK'
        }, 201

    @jwt_required
    def delete(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()
        todo_name = request.json['todo_name']

        todo_list = list()

        for i in mirror['todo']:
            print('DELETE {}'.format(i['name']), 'GET UP {}'.format(todo_name))
            if not i['name'] == todo_name:
                todo_list.append(i)

        mirror.update(
            todo=todo_list
        )

        mirror.save()

        sio = socketio.Client()
        sio.connect('http://{}:{}'.format('127.0.0.1', 5556))
        sio.emit('show_todo', {
            'key': get_jwt_identity()
        })

        return '', 200