from marshmallow import Schema

class SettlementSchema(Schema):
    
    class Meta:
        fields = ('pk_asentamiento', 'd_codigo', 'd_asenta', 'd_tipo_asenta',
                  'D_mnpio', 'd_estado', 'd_ciudad', 'd_CP', 'c_estado',
                  'c_oficina', 'c_CP', 'c_tipo_asenta', 'c_mnpio',
                  'id_asenta_cpcons', 'd_zona', 'c_cve_ciudad')
        ordered = True
        
settlements_schema = SettlementSchema(many=True)
settlement_schema = SettlementSchema()



class StatesSchema(Schema):

    class Meta:
        fields = ('c_estado', 'd_estado')
        ordered = True

states_schema = StatesSchema(many=True)
state_schema = StatesSchema()


class MunicipalitySchema(Schema):

    class Meta:
        fields = ('c_mnpio', 'D_mnpio')
        ordered = True

municipalities_schema = MunicipalitySchema(many=True)
municipality_schema = MunicipalitySchema()


class SettlementTypeSchema(Schema):

    class Meta:
        fields = ('c_tipo_asenta', 'd_tipo_asenta')
        ordered = True

settlements_type_schema = SettlementTypeSchema(many=True)
settlement_type_schema = SettlementTypeSchema()