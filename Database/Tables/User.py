from sqlalchemy import *

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('nation_id', String(60)),
             Column('name', String(16), nullable=False),
             Column('phone_number', String(50), nullable=False),
             Column('user_description', String(50), nullable=False))
