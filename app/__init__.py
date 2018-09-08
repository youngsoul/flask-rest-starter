import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from app.resources.v1.SecretResource import SecretResource
from app.services.jwt_services import check_if_token_in_blacklist
from flask_restful import Api
from app.models import UserModel
from app.services import db_services

from flask_jwt_extended import JWTManager
from app.services.jwt_services import check_if_token_in_blacklist


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # usually try to use flask blueprints to break up the application and register
    # the resources within the blueprint
    from app.resources.v1.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/v1/auth')

    from app.resources.v1.users import user_bp
    app.register_blueprint(user_bp, url_prefix='/v1/users')

    from app.resources.v1.unsecured import unsecured_bp
    app.register_blueprint(unsecured_bp, url_prefix='/v1/unsecured')


    # resources can also be added directly in thie create_app function
    api = Api(app)

    api.add_resource(SecretResource, '/secret')

    # Create the JWTManager and associate it with the Flask app
    # Configuration: https://flask-jwt-extended.readthedocs.io/en/latest/options.html#configuration-options
    jwt = JWTManager(app)

    # Initialize the users from the config
    existing_users = config_class.load_users()
    for user in existing_users:
        user = UserModel(user['username'], user['password'])
        db_services.save_user(user)

    # Access tokens by default have a timeout of 15 minutes, and refresh tokens have a timeout of 30 days
    # to logout, or prematurely force a token to expire, it must be placed on a blacklist and that blacklist
    # needs to be checked.
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

