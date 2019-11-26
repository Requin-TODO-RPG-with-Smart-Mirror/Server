from datetime import timedelta

EXPIRE_TIME = timedelta(minutes=100000)

class LocalApplicationConfig:
    ENV = "local"
    DEBUG = True

    JWT_ACCESS_TOKEN_EXPIRES = EXPIRE_TIME
    JWT_REFRESH_TOKEN_EXPIRES = EXPIRE_TIME

    SECRET_KEY = '_7H1S_1S_S3CR37_K3Y'