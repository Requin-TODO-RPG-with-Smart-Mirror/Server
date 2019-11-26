from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token

import key_list


api = Api(Blueprint(__name__, __name__))
api.prefix = '/mirror'

@api.resource('/register/key')
class RegisterManagement(Resource):
    def post(self):
        key_value = request.json['key']

        if key_value not in key_list.KEY_LIST:
            abort(403)

        return {
            'access_token':create_access_token(identity=key_value),
            'status':'OK'
        }, 201

