##basedata table

from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from config.db import meta , engine
from schemas.person import HairColor
from sqlalchemy import Enum


persons = Table(
    'persons',
    meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(255)),
    Column('last_name',String(255)),
    Column('age', Integer),
    Column('hair_color',Enum(HairColor))
)

meta.create_all(engine)