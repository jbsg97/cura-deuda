from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    VARCHAR
)
from src.config.db import db

class Settlement(db.Model):
    __tablename__ = 'asentamientos'
    __table_args__ = {'implicit_returning': False}
    pk_asentamiento = Column(Integer, primary_key=True, nullable=False)
    d_codigo = Column(Integer)
    d_asenta = Column(VARCHAR(length=250))
    d_ciudad = Column(VARCHAR(length=250))
    d_CP = Column(Integer)
    c_estado = Column(Integer)
    c_oficina = Column(Integer)
    c_CP = Column(VARCHAR(length=100))
    c_tipo_asenta = Column(Integer)
    c_mnpio = Column(Integer)
    id_asenta_cpcons = Column(Integer)
    d_zona = Column(VARCHAR(length=250))
    c_cve_ciudad = Column(Integer)


class States(db.Model):
    __tablename__ = 'estados'
    __table_args__ = {'implicit_returning': False}
    c_estado = Column(Integer, primary_key=True, nullable=False)
    d_estado = Column(VARCHAR(length=250))


class Municipality(db.Model):
    __tablename__ = 'municipios'
    __table_args__ = {'implicit_returning': False}
    c_mnpio = Column(Integer, primary_key=True, nullable=False)
    D_mnpio = Column(VARCHAR(length=250))


class SettlementType(db.Model):
    __tablename__ = 'tipos_asentamientos'
    __table_args__ = {'implicit_returning': False}
    c_tipo_asenta = Column(Integer, primary_key=True, nullable=False)
    d_tipo_asenta = Column(VARCHAR(length=250))