from flask_restful import Resource, request
from src.app.services.settlement import (
    SettlementService,
    StateService,
    MunicipalityService,
    SettlementTypeService
)
from src.app.validators.settlement import (
    SettlementValidator,
    StateValidator,
    MunicipalityValidator,
    SettlementTypeValidator
)
from flask_jwt_extended import jwt_required

class SettlementController(Resource, SettlementValidator):
    def __init__(self):
        self.settlement_service = SettlementService()

    def get(self):
        postal_code = None if not request.args\
            .get('postal_code') else request.args.get('postal_code')
        settlement = None if not request.args\
            .get('settlement') else request.args.get('settlement')
        municipality = None if not request.args\
            .get('municipality') else request.args.get('municipality')
        state = None if not request.args\
            .get('state') else request.args.get('state')

        data = self.settlement_service.fetch(postal_code, settlement,
                                             municipality, state)
        if not data:
            return {'data': [], 'message': 'No se encontrarón asentamientos.'}, 404
        return {'data': data, 'message': 'success'}, 200

    @jwt_required()
    def post(self):
        body = self.parser.parse_args()
        data = self.settlement_service.create(**body)

        if not data:
            return {'data': [], 'message': 'No se pudo insertar asentamiento'}, 404
        return {'data': data, 'message': 'success'}, 200


class StateController(Resource, StateValidator):
    def __init__(self):
        self.state_service = StateService()

    def get(self):
        state = None if not request.args\
            .get('state') else request.args.get('state')
        data = self.state_service.fetch(state)
        if not data:
            return {'data': [], 'message': 'No se encontrarón estados.'}, 404
        return {'data': data, 'message': 'success'}, 200

    @jwt_required()
    def post(self):
        body = self.parser.parse_args()
        data = self.state_service.create(**body)

        if not data:
            return {'data': [], 'message': 'No se pudo insertar estado.'}, 404
        return {'data': data, 'message': 'success'}, 200


class MunicipalityController(Resource, MunicipalityValidator):
    def __init__(self):
        self.municipality_service = MunicipalityService()

    def get(self):
        municipality = None if not request.args\
            .get('municipality') else request.args.get('municipality')
        data = self.municipality_service.fetch(municipality)
        if not data:
            return {'data': [], 'message': 'No se encontrarón municipios.'}, 404
        return {'data': data, 'message': 'success'}, 200

    @jwt_required()
    def post(self):
        body = self.parser.parse_args()
        data = self.municipality_service.create(**body)

        if not data:
            return {'data': [], 'message': 'No se pudo insertar municipio.'}, 404
        return {'data': data, 'message': 'success'}, 200


class SettlementTypeController(Resource, SettlementTypeValidator):
    def __init__(self):
        self.settlement_type_service = SettlementTypeService()

    def get(self):
        settlement_type = None if not request.args\
            .get('settlement_type') else request.args.get('settlement_type')
        data = self.settlement_type_service.fetch(settlement_type)
        if not data:
            return {'data': [], 'message': 'No se encontrarón tipos de asentamientos.'}, 404
        return {'data': data, 'message': 'success'}, 200

    @jwt_required()
    def post(self):
        body = self.parser.parse_args()
        data = self.settlement_type_service.create(**body)

        if not data:
            return {'data': [], 'message': 'No se pudo insertar tipo asentamiento.'}, 404
        return {'data': data, 'message': 'success'}, 200
