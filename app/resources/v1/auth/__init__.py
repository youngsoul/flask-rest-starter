from flask import Blueprint
from flask_restful import Api, reqparse
from app.resources.v1.auth.UserRegistration import UserRegistration
from app.resources.v1.auth.UserLogin import UserLogin
from app.resources.v1.auth.TokenRefresh import TokenRefresh
from app.resources.v1.auth.UserLogoutAccess import UserLogoutAccess
from app.resources.v1.auth.UserLogoutRefresh import UserLogoutRefresh

auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)


api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
