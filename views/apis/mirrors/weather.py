import requests
import random
import socketio

from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.mirror import MirrorModel


api = Api(Blueprint(__name__, __name__))


@api.resource('/weather')
class RegisterTodoManagement(Resource):
    def get(self):
        url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

        querystring = {"zone": "1168066000"}

        headers = {
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "/",
            'Cache-Control': "no-cache",
            'Postman-Token': "f57c618c-37d3-4e05-ad5a-365d74cd05e8,71fbf16e-5384-4a77-823f-f645a8ac4fef",
            'Host': "www.kma.go.kr",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

        return {
            'weather':response.text,
            'status':'OK'
        }, 201
