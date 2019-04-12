from sqlalchemy.ext.declarative import declarative_base

from Database.Tables.Admin import *
from Database.Tables.Helps import *
from Database.Tables.User import *
from database import database
from Config.bot_config import BotConfig


def migrate():
    engine = create_engine('sqlite:///charity.sqlite')
    connection = engine.connect()
    metadata = MetaData()

    Base = declarative_base()

    if not engine.dialect.has_table(engine, admin.name):
        metadata.create_all(engine, tables={admin})

    if not engine.dialect.has_table(engine, user.name):
        metadata.create_all(engine, tables={user})

    if not engine.dialect.has_table(engine, help_table.name):
        metadata.create_all(engine, tables={help_table})

    if not database().is_admin(BotConfig.first_admin):
        database().insert_admin(BotConfig.first_admin)

    query = select([admin])
    ResultProxy2 = connection.execute(query)
    ResultSet = ResultProxy2.fetchall()
    print("admins : " + str(ResultSet))
