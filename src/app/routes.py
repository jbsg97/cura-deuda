from flask import Blueprint
from flask_restful import Api

from src.app.controllers.settlement import (
    SettlementController,
    StateController,
    MunicipalityController,
    SettlementTypeController
)

blueprint_urls = Blueprint('url_global', __name__)
api = Api(blueprint_urls, prefix='/api')

api.add_resource(SettlementController, '/settlements')
api.add_resource(StateController, '/states')
api.add_resource(MunicipalityController, '/municipality')
api.add_resource(SettlementTypeController, '/settlements/types')