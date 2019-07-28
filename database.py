import sqlalchemy as db
from Database.Tables.Admin import *
from Database.Tables.Helps import *
from Database.Tables.User import *


class database:
    engine = db.create_engine('sqlite:///charity.sqlite', connect_args={'check_same_thread': False})
    connection = engine.connect()

    def insert_admin(self, username):
        query = db.insert(admin).values(username=username)
        ResultProxy = self.connection.execute(query)
        return ResultProxy

    def is_exist_user(self, nationid, phonenumber):
        query = db.select([user]).where(
            db.or_(user.columns.nation_id == nationid, user.columns.phone_number == phonenumber))
        result = self.connection.execute(query)
        result_set = result.fetchall()
        return len(result_set) != 0

    def is_admin(self, username):
        query = db.select([admin]).where(admin.columns.username == username)
        result = self.connection.execute(query)
        result_set = result.fetchall()
        return len(result_set) != 0

    def is_exist_user_by_id(self, user_id):
        query = db.select([user]).where(user.columns.id == int(user_id))
        result = self.connection.execute(query)
        result_set = result.fetchall()
        return len(result_set) != 0

    def is_exist_user_by_nation_id(self, nation_id):
        query = db.select([user]).where(user.columns.nation_id == nation_id)
        result = self.connection.execute(query)
        result_set = result.fetchall()
        return len(result_set) != 0

    def insert_user(self, name, phonenumber, nationid, description):
        query = db.insert(user).values(name=name, nation_id=nationid, phone_number=phonenumber,
                                       user_description=description)
        ResultProxy = self.connection.execute(query)
        return True

    def remove_user(self, nation_id):
        query = db.delete(user).where(user.columns.nation_id == nation_id)
        ResultProxy = self.connection.execute(query)
        return True

    def insert_help(self, nation_id, amount, descripition):
        query = db.insert(help_table).values(nation_id=nation_id, amount=amount, description=descripition)
        ResultProxy = self.connection.execute(query)
        return True

    def get_all_user(self):
        query = select([user])
        ResultProxy2 = self.connection.execute(query)
        ResultSet = ResultProxy2.fetchall()
        return ResultSet

    def get_all_helps(self):
        query = select([help_table, user])
        query = query.select_from(help_table.join(user, user.columns.nation_id == help_table.columns.nation_id))
        ResultProxy2 = self.connection.execute(query)
        ResultSet = ResultProxy2.fetchall()
        return ResultSet

    def get_all_helps_order_by_user_id(self, user_id):
        query = select([help_table]).where(help_table.columns.user_id == user_id)
        ResultProxy2 = self.connection.execute(query)
        ResultSet = ResultProxy2.fetchall()
        return ResultSet

    def get_all_helps_order_by_nation_id(self, nation_id):
        query = select([help_table]).where(help_table.columns.nation_id == nation_id)
        ResultProxy2 = self.connection.execute(query)
        ResultSet = ResultProxy2.fetchall()
        return ResultSet
