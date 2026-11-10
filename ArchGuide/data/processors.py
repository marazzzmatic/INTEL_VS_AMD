import sqlalchemy
from sqlalchemy import orm
from db_session import SqlAlchemyBase


class Processor(SqlAlchemyBase):
    __table_name__ = "processors"
    # основное
    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    brand = sqlalchemy.Column(sqlalchemy.String)

    # характеристики процессора
    cores = sqlalchemy.Column(sqlalchemy.Integer)
    threads = sqlalchemy.Column(sqlalchemy.Integer)
    cache_l3 = sqlalchemy.Column(sqlalchemy.Integer)  # в МБ
    tdp = sqlalchemy.Column(sqlalchemy.Integer)  # в Ваттах
    price = sqlalchemy.Column(sqlalchemy.Integer)
