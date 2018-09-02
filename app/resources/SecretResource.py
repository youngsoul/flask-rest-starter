from flask_restful import Resource


class SecretResource(Resource):

    def get(self):
        return {
            'answer': 42
        }

