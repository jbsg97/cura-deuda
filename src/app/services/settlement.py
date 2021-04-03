from src.config.db import db
from src.app.serializers.settlement import (
    settlements_schema,
    settlement_schema,
    states_schema,
    state_schema,
    municipalities_schema,
    municipality_schema,
    settlements_type_schema,
    settlement_type_schema
)
from src.app.models.settlement import (
    Settlement,
    States,
    Municipality,
    SettlementType
)
from sqlalchemy import exc as SQLAlchemyError

class SettlementService:
    _instance = None

    def create(self, **kwargs):
        data = Settlement(**kwargs)
        try:
            db.session.add(data)
            db.session.commit()
            return settlement_schema.dump(data)
        except SQLAlchemyError as e:
            db.session.rollback()
            return None

    def fetch(self, postal_code, settlement, municipality, state):
        settlements = db.session\
        .query(
            Settlement.pk_asentamiento,
            Settlement.d_codigo,
            Settlement.d_asenta,
            SettlementType.d_tipo_asenta,
            Municipality.D_mnpio,
            States.d_estado,
            Settlement.d_ciudad,
            Settlement.d_CP,
            States.c_estado,
            Settlement.c_oficina,
            Settlement.c_CP,
            SettlementType.c_tipo_asenta,
            Municipality.c_mnpio,
            Settlement.id_asenta_cpcons,
            Settlement.d_zona,
            Settlement.c_cve_ciudad
        )\
        .join(States, States.c_estado == Settlement.c_estado)\
        .join(Municipality, Municipality.c_mnpio == Settlement.c_mnpio)\
        .join(SettlementType, SettlementType.c_tipo_asenta == Settlement.c_tipo_asenta)
        
        if postal_code != None:
            settlements = settlements.filter(
                Settlement.d_codigo == int(postal_code)
            )
        
        if settlement != None:
            settlements = settlements.filter(
                Settlement.d_asenta == settlement
            )
        
        if municipality != None:
            settlements = settlements.filter(
                Municipality.D_mnpio == municipality
            )
        
        if state != None:
            settlements = settlements.filter(
                States.d_estado == state
            )
        
        settlements = settlements.all()
        return settlements_schema.dump(settlements) if settlements else None


class StateService:
    _instance = None

    def create(self, **kwargs):
        try:
            d_state = kwargs['d_estado']
            c_state = kwargs['c_estado']
            query = f"INSERT INTO estados VALUES('{d_state}', {c_state})"
            db.session.execute(query)
            db.session.commit()
            return state_schema.dump(kwargs)
        except Exception as e:
            print(e)
            db.session.rollback()
            return None
    
    def fetch(self, state):
        states = States.query
        if state != None:
            states = states.filter(States.d_estado == state)
        states = states.all()

        return states_schema.dump(states) if states else None


class MunicipalityService:
    _instance = None

    def create(self, **kwargs):
        try:
            d_municipality = kwargs['D_mnpio']
            c_municipality = kwargs['c_mnpio']
            query = f"INSERT INTO municipios VALUES('{d_municipality}', {c_municipality})"
            db.session.execute(query)
            db.session.commit()
            return municipality_schema.dump(kwargs)
        except Exception as e:
            db.session.rollback()
            return None
    
    def fetch(self, municipality):
        municipalities = Municipality.query
        if municipality != None:
            municipalities = municipalities.filter(Municipality.D_mnpio == municipality)
        municipalities = municipalities.all()

        return municipalities_schema.dump(municipalities) if municipalities else None


class SettlementTypeService:
    _instance = None

    def create(self, **kwargs):
        try:
            d_settlement_type = kwargs['d_tipo_asenta']
            c_settlement_type = kwargs['c_tipo_asenta']
            query = f"INSERT INTO tipos_asentamientos VALUES('{d_settlement_type}', {c_settlement_type})"
            db.session.execute(query)
            db.session.commit()
            return settlement_type_schema.dump(kwargs)
        except Exception as e:
            db.session.rollback()
            return None

    def fetch(self, settlement_type):
        settlement_types = SettlementType.query
        if settlement_type != None:
            settlement_types = settlement_types.filter(SettlementType.d_tipo_asenta == settlement_type)
        settlement_types = settlement_types.all()

        return settlements_type_schema.dump(settlement_types) if settlement_types else None