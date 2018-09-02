from flask_restful import Resource

class TokenRefresh(Resource):

    def post(self):
        return {'message': 'Token Refresh Post'}


