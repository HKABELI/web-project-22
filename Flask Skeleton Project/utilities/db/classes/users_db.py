from utilities.db.db_manager import dbManager


class UsersDb:

    @staticmethod
    def insert_user(email, first_name, last_name, password, phone_number):
        query = "INSERT INTO users(email,first_name,last_name,password,phone_number) VALUES ('%s','%s','%s','%s','%s')" % (
            email, first_name, last_name, password, phone_number)
        return dbManager.commit(query)

    @staticmethod
    def delete_user_by_email(email):
        query = "DELETE FROM  users WHERE email='%s'" % email
        return dbManager.commit(query)

    @staticmethod
    def get_all_users():
        query = "select * from users"
        query_result = dbManager.fetch(query)
        return query_result

    @staticmethod
    def is_user_exist(email, first_name, phone_number):
        exist_query = "SELECT email AS count FROM users WHERE email = '%s'  AND first_name = '%s' AND  phone_number = '%s' " % (
            email, first_name, phone_number)
        result = dbManager.fetch(exist_query)
        return result

    @staticmethod
    def is_email_exist(email):
        exist_query = "SELECT email as count FROM users where email = '%s'" % email
        result = dbManager.fetch(exist_query)
        return result

