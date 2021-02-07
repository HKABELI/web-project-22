from utilities.db.db_manager import dbManager


class EXdb:


    @staticmethod
    def get_all_exercises():
        exercises_list_query = ("SELECT * FROM exercises")
        result = dbManager.fetch(exercises_list_query)
        return result

    @staticmethod
    def add_exercises(name, fromTime, toTime, dayOfWeek, capacity, address):
        insert_exercise_query = ("INSERT INTO exercises (name,fromTime,"
                                 " toTime,dayOfWeek,capacity,address) VALUES ("
                                 "'%s','%s','%s',%s,%s,'%s')" %
                                 (name, fromTime, toTime, dayOfWeek, capacity, address))
        result = dbManager.commit(insert_exercise_query)
        return result

    @staticmethod
    def delete_exercise_by_id(exerciseID):
        delete_query = "DELETE FROM exercises where exercisesID=%s" % exerciseID
        return dbManager.commit(delete_query)




    @staticmethod
    def display_exercise_by_id(exerciseID):
        select_exerciseQuery = ("SELECT * FROM exercises where exercisesID=%s" % exerciseID)
        result = dbManager.fetch(select_exerciseQuery)


