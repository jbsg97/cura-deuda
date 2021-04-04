from flask_restful import Resource, request
from src.app.services.administration import UserService
from src.app.validators.administration import UserValidator
from flask_jwt_extended import jwt_required

class UserController(Resource, UserValidator):
    def __init__(self):
        self.users_service = UserService()

    @jwt_required()
    def get(self):
        data = self.users_service.fetch()
        if not data:
            return {'data': [], 'message': 'No se encontrarón usuarios.'}, 404
        return {'data': data, 'message': 'success'}, 200

    @jwt_required()
    def post(self):
        body = self.parser.parse_args()
        data = self.users_service.create(**body)
        if not data:
            return {'data': [], 'message': 'Error al crear usuario.'}, 404
        return {'data': data, 'message': 'success'}, 200
