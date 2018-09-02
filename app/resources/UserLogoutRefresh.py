from flask_restful import Resource

class UserLogoutRefresh(Resource):

    def post(self):
        return {'message': 'UserLogoutRefresh Post'}
    