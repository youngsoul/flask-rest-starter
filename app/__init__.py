import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from app.resources.AllUsers import AllUsers
from app.resources.SecretResource import SecretResource
from app.resources.TokenRefresh import TokenRefresh
from app.resources.UserLogin import UserLogin
from app.resources.UserLogoutAccess import UserLogoutAccess
from app.resources.UserLogoutRefresh import UserLogoutRefresh
from app.resources.UserRegistration import UserRegistration

from flask_restful import Api

def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(app)

    api.add_resource(AllUsers, '/users')
    api.add_resource(UserRegistration, '/registration')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogoutAccess, '/logout/access')
    api.add_resource(UserLogoutRefresh, '/logout/refresh')
    api.add_resource(TokenRefresh, '/token/refresh')
    api.add_resource(SecretResource, '/secret')

    try:
        if not app.debug and not app.testing:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/app_logs.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

            app.logger.setLevel(logging.INFO)
            app.logger.info('Flask Starter startup')
    except:
        # if for any reason we cannot save the file logger.. skip it.
        # this can happen if we are using zappa to deploy to the AWS Lambda
        pass

    return app

