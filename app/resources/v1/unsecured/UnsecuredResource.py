from flask_restful import Resource


class UnsecuredResource(Resource):

    def get(self):
        return {'msg': "unsecured resource return"}



