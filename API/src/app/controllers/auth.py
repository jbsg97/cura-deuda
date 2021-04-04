from flask_restful import Resource, request
from src.app.services.auth import AuthService

class AuthController(Resource):
    def __init__(self):
        self.auth_service = AuthService()
    
    def post(self):
        body = request.get_json()
        token = self.auth_service.get_token(**body)
        if not token:
            return {'data': [], 'message': 'Credenciales incorrectas.'}, 404
        return {'access_token': token, 'message': 'success'}, 200
