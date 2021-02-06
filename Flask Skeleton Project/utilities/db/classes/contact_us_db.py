from utilities.db.db_manager import dbManager


class ContactUsDb:

    @staticmethod
    def insert_message(email, first_name, phone_number, message):
        # if user in the user list
        query = "INSERT INTO contact_us(email,first_name,phone_number,message) VALUES ('%s','%s','%s','%s')" % (
            email, first_name, phone_number, message)
        dbManager.commit(query)

    @staticmethod
    def delete_message_by_email(email):
        query = "DELETE FROM  contact_us WHERE email='%s'" % email
        return dbManager.commit(query)

    @staticmethod
    def get_all_messages():
        query = "select * from contact_us"
        query_result = dbManager.fetch(query)
        return query_result

    @staticmethod
    def get_message_by_user_email(email):
        query = "SELECT * FROM  contact_us WHERE email='%s'" % email
        return dbManager.fetch(query)


    @staticmethod
    def get_all_messages_in_month(month):
        query = "SELECT * FROM  contact_us WHERE MONTH(message_date) ='%s'" % month
        return dbManager.fetch(query)

