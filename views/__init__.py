from flask import Flask
from mongoengine import connect
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from views.router import Router
from const import _MONGO_SETTING



def create_app(*config_cls) -> Flask:
    _app = Flask(__name__)

    for config in config_cls:
        _app.config.from_object(config)

    CORS(_app, resources={
        r"*": {"origin": "*"},
    })
    Router(_app)
    connect(**_MONGO_SETTING)
    JWTManager().init_app(_app)

    return _app