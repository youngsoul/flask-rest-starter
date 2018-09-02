from flask_restful import Resource

class UserLogin(Resource):

    def post(self):
        return {'message': 'User Login Post'}

