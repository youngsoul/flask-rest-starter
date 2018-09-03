from flask_restful import Resource
from .parsers import up_parser
from app.models import UserModel
from app.services import db_services
from flask_jwt_extended import (create_access_token,
                                create_refresh_token)

class UserRegistration(Resource):

    def post(self):
        try:
            data = up_parser.parse_args()
            if db_services.find_by_username(data['username']) is None:
                user = UserModel(data['username'], data['password'])
                db_services.save_user(user)
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])
                return {
                    'message': 'User {} was created'.format(data['username']),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            else:
                return {'message': 'User already exists'}, 500
        except:
            return {'message': 'Something went wrong'}, 500
