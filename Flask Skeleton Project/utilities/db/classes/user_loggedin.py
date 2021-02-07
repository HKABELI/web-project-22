from utilities.db.db_manager import dbManager


class UsersLG:

    @staticmethod
    def insert_login_user(email):
        insert_loggedin = "INSERT INTO loggedin (email) values('%s')" % (
                email)
        query1 = dbManager.commit(insert_loggedin)
        return query1
