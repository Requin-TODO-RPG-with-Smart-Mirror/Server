import random
import socketio

from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.mirror import MirrorModel


api = Api(Blueprint(__name__, __name__))
api.prefix = '/todo'

@api.resource('/check')
class RegisterTodoManagement(Resource):
    @jwt_required
    def post(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()
        todo_name: str = request.json['todo_name']

        todo_list = list()

        update_exp = int()
        update_money = int()

        for i in mirror['todo']:
            if not i['name'] == todo_name:
                todo_list.append(i)
            else:
                if i['check'] == False:
                    i['check'] = True
                    update_exp = i['important'] * random.randrange(5, 20)
                    update_money = i['important'] * random.randrange(5, 20)
                    todo_list.append(i)

        mirror.update(
            todo=todo_list,
            exp = mirror['exp'] + update_exp,
            money = mirror['money'] + update_money
        )

        if mirror['exp'] + update_exp > 5000:
            mirror.update(
                level = 10
            )

            mirror.stuff.append(
                'skin-0-9'
            )

        elif mirror['exp'] + update_exp > 4000:
            mirror.update(
                level = 9
            )

            mirror.stuff.append(
                'skin-0-8'
            )

        elif mirror['exp'] + update_exp > 2000:
            mirror.update(
                level = 8
            )

            mirror.stuff.append(
                'skin-0-7'
            )

        elif mirror['exp'] + update_exp > 1000:
            mirror.update(
                level = 7
            )

            mirror.stuff.append(
                'skin-0-6'
            )

        elif mirror['exp'] + update_exp > 300:
            mirror.update(
                level = 6
            )

            mirror.stuff.append(
                'skin-0-5'
            )

        elif mirror['exp'] + update_exp > 150:
            mirror.update(
                level = 5
            )

            mirror.stuff.append(
                'skin-0-4'
            )

        elif mirror['exp'] + update_exp > 100:
            mirror.update(
                level = 4
            )

            mirror.stuff.append(
                'skin-0-3'
            )

        elif mirror['exp'] + update_exp > 50:
            mirror.update(
                level = 3
            )

            mirror.stuff.append(
                'skin-0-2'
            )

        elif mirror['exp'] + update_exp > 20:
            mirror.update(
                level = 2
            )

            mirror.stuff.append(
                'skin-0-1'
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