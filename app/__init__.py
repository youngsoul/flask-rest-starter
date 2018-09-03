import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from app.resources.v1.SecretResource import SecretResource
from app.services.jwt_services import check_if_token_in_blacklist
from flask_restful import Api

from flask_jwt_extended import JWTManager
from app.services.jwt_services import check_if_token_in_blacklist


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.resources.v1.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/v1/auth')

    from app.resources.v1.users import user_bp
    app.register_blueprint(user_bp, url_prefix='/v1/users')

    api = Api(app)

    api.add_resource(SecretResource, '/secret')

    jwt = JWTManager(app)

    @jwt.token_in_blacklist_loader
    def token_check(decrypted_token):
        return check_if_token_in_blacklist(decrypted_token)

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

