from flask_restful import Api
from flask import Blueprint
from app.resources.v1.users.AllUsers import AllUsers

user_bp = Blueprint('users', __name__)
api = Api(user_bp)


api.add_resource(AllUsers, '/all')
