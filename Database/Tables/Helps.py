from sqlalchemy import *

metadata = MetaData()

help_table = Table('help', metadata,
                   Column('hid', Integer, primary_key=True),
                   Column('user_id', Integer),
                   Column('nation_id', String(60)),
                   Column('amount', String(16), nullable=False),
                   Column('description', String(60)))
