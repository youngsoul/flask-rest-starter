from flask_restful import Resource
from .parsers import up_parser
from app.services import db_services
from flask_jwt_extended import create_access_token, create_refresh_token

class UserLogin(Resource):

    def post(self):
        try:
            data = up_parser.parse_args()
            user = db_services.find_by_username(data['username'])
            if user is not None and data['password'] == user.password:
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])
                return {
                    'message': 'User {} was created'.format(data['username']),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            else:
                return {'message': 'User does not exists'}, 500
        except Exception as exc:
            print(exc)
            return {'message': 'Something went wrong'}, 500

