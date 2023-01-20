##basedata table

from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from config.db import meta , engine


persons = Table(
    'persons',
    meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(255)),
    Column('last_name',String(255))
)

meta.create_all(engine)