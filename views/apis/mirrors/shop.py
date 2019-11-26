import socketio

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from stuffs import skin
from models.mirror import MirrorModel


api = Api(Blueprint(__name__, __name__))
api.prefix = '/mirror'

@api.resource('/shop')
class RegisterCharManagement(Resource):
    @jwt_required
    def get(self):

        return {
            'skin_list': skin
        }

    @jwt_required
    def post(self):
        mirror = MirrorModel.objects(mirror_key=get_jwt_identity()).first()
        item = request.json['skin']
        item_money = request.json['money']

        if not (item in skin):
            abort(409)

        if mirror['money'] < item_money:
            abort(403)

        if item in mirror['stuff']:
            abort(412)

        mirror.stuff.append(
            item
        )

        mirror.update(
            exp = mirror['money'] - item_money
        )

        mirror.save()

        return {
            'status':'OK'
        }, 201

