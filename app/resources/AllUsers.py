from flask_restful import Resource

class AllUsers(Resource):

    def get(self):
        return {'message': 'List of users'}


    def delete(self):
        return {'message': 'Delete all users'}


