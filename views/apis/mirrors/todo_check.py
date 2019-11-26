from flask import Blueprint, request, abort
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

        for i in mirror['todo']:
            if not i['name'] == todo_name:
                todo_list.append(i)
            else:
                if i['check'] == False:
                    i['check'] = True
                    update_exp += i['important'] * 20
                    todo_list.append(i)
                else:
                    i['check'] = False
                    update_exp -= i['important'] * 20
                    todo_list.append(i)

        mirror.update(
            todo=todo_list,
            exp = mirror['exp'] + update_exp
        )

        mirror.save()

        return {
            'status':'OK'
        }, 201