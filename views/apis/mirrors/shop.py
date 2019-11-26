import socketio

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from stuffs import head, body
from models.mirror import MirrorModel


api = Api(Blueprint(__name__, __name__))
api.prefix = '/mirror'

@api.resource('/shop')
class RegisterCharManagement(Resource):
    @jwt_required
    def get(self):

        return {
            'head_list': head,
            'body_list': body
        }

    @jwt_required
    def post(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()
        item = request.json['item']
        item_exp = request.json['exp']

        if not (item in head or item in body):
            abort(409)

        if mirror['exp'] < item_exp:
            abort(403)

        if item in mirror['stuff']:
            abort(412)

        mirror.stuff.append(
            item
        )

        mirror.save()

        return {
            'status':'OK'
        }, 201

