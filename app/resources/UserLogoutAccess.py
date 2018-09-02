from flask_restful import Resource

class UserLogoutAccess(Resource):

    def post(self):
        return {'message': 'user Logout post'}


