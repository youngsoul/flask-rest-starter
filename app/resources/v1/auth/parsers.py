from flask_restful import reqparse


up_parser = reqparse.RequestParser()
up_parser.add_argument('username', help='This field cannot be blank', required=True)
up_parser.add_argument('password', help='This field cannot be blank', required=True)
