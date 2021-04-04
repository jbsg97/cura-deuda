from flask_restful import reqparse

class UserValidator:
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Se requiere el campo username')
    parser.add_argument('password', type=str, required=True, help='Se requiere el campo password')