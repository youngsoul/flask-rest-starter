from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username')
class UserRegistration(Resource):

    def post(self):
        return {'message': 'User Registration Post'}

