import socketio

from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.mirror import MirrorModel


api = Api(Blueprint(__name__, __name__))
api.prefix = '/mirror'

@api.resource('/register/char')
class RegisterCharManagement(Resource):
    @jwt_required
    def post(self):
        name = request.json['name']

        MirrorModel(
            mirror_key = get_jwt_identity(),

            name = name,

            exp = 0,

            money = 0,

            level = 1,

            skin = 'skin-0-0',

            stuff = ['skin-0-1','skin-0-2','skin-0-3','skin-0-4','skin-0-5','skin-0-6','skin-0-7','skin-0-8','skin-0-9','skin-0-0'],

            todo = []
        ).save()

        sio = socketio.Client()
        sio.connect('http://{}:{}'.format('127.0.0.1', 5556))
        sio.emit('register', {
            'key':get_jwt_identity(),
        })

        return {
            'status':'OK'
        }, 201

