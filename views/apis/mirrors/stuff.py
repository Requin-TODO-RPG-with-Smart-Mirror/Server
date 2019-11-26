import socketio

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from stuffs import head, body
from models.mirror import MirrorModel

api = Api(Blueprint(__name__, __name__))
api.prefix = '/mirror'


@api.resource('/stuff')
class RegisterCharManagement(Resource):
    @jwt_required
    def get(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()

        return {
            'stuff_list': mirror['stuff']
        }

    @jwt_required
    def post(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()
        stuff = request.json['stuff']

        if stuff not in mirror['stuff']:
            abort(409)

        if 'head' in stuff:
            mirror.update(
                character = {'head': stuff}
            )

        else:
            mirror.update(
                character = {'body': stuff}
            )

        sio = socketio.Client()
        sio.connect('http://{}:{}'.format('127.0.0.1', 5556))
        sio.emit('now_look', {
            'key': get_jwt_identity(),
        })

        return {

        }, 201


