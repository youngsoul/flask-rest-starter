from flask_restful import Api
from flask import Blueprint
from app.resources.v1.unsecured.UnsecuredResource import UnsecuredResource

unsecured_bp = Blueprint('unsecured', __name__)
api = Api(unsecured_bp)


api.add_resource(UnsecuredResource, '/OU812')
