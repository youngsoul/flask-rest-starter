from flask_restful import Resource
from app.services.db_services import get_all_users, delete_all_users
from flask_jwt_extended import jwt_required

class AllUsers(Resource):

    @jwt_required
    def get(self):
        all_users = get_all_users()
        return {'users': [f"{u}" for u in all_users]}

    @jwt_required
    def delete(self):
        n = delete_all_users()
        return {'message': f" deleted {n} users"}


