from sqlalchemy import *

metadata = MetaData()

admin = Table('admin', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String(200), nullable=False))
