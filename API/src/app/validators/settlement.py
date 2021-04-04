from flask_restful import reqparse

class SettlementValidator:
    parser = reqparse.RequestParser()
    parser.add_argument('d_codigo', type=int, required=True, help='Se requiere codigo de asentamiento')
    parser.add_argument('d_asenta', type=str, required=True, help='Se requiere nombre de asentamiento')
    parser.add_argument('d_CP', type=int, required=True, help='Se requiere Código Postal de la Administración Postal')
    parser.add_argument('c_estado', type=int, required=True, help='Se requiere Clave Entidad')
    parser.add_argument('c_oficina', type=int, required=True, help='Se requiere Código Postal de la Administración Postal')
    parser.add_argument('c_CP', type=str, required=False, default = '0')
    parser.add_argument('c_tipo_asenta', type=int, required=True, help='Se requiere Clave Tipo de asentamiento')
    parser.add_argument('c_mnpio', type=int, required=True, help='Se requiere Clave Municipio')
    parser.add_argument('id_asenta_cpcons', type=int, required=True, help='Se requiere Identificador único del asentamiento')
    parser.add_argument('d_zona', type=str, required=True, help='Se requiere Zona en la que se ubica el asentamiento (Urbano/Rural)')
    parser.add_argument('c_cve_ciudad', type=int, required=True, help='Se requiere Clave Ciudad')


class StateValidator:
    parser = reqparse.RequestParser()
    parser.add_argument('c_estado', type=int, required=True, help='Se requiere codigo de estado')
    parser.add_argument('d_estado', type=str, required=True, help='Se requiere nombre de estado')


class MunicipalityValidator:
    parser = reqparse.RequestParser()
    parser.add_argument('c_mnpio', type=int, required=True, help='Se requiere codigo de municipio')
    parser.add_argument('D_mnpio', type=str, required=True, help='Se requiere nombre de municipio')


class SettlementTypeValidator:
    parser = reqparse.RequestParser()
    parser.add_argument('c_tipo_asenta', type=int, required=True, help='Se requiere codigo de tipo asentamiento')
    parser.add_argument('d_tipo_asenta', type=str, required=True, help='Se requiere nombre de tipo asentamiento')
