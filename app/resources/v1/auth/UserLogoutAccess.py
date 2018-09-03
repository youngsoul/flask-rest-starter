from flask_restful import Resource
from flask_jwt_extended import (jwt_required,
                                get_raw_jwt)
from app.services.jwt_services import add_revoked_token

class UserLogoutAccess(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            add_revoked_token(jti)
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500

