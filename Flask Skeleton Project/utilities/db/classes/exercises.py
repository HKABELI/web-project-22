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
    def edit_exercises(name, fromTime, toTime, dayOfWeek, capacity, address):
         update_exercise_query = ("UPDATE exercises  SET name='%s',"
                             "fromTime='%s',"
                             " toTime='%s',"
                             "dayOfWeek=%s,"
                             "capacity=%s,"
                             "address='%s' WHERE exercisesID=%s" %
                             (name, fromTime, toTime, dayOfWeek, capacity, address))
         result = dbManager.commit(update_exercise_query)
         return result

    @staticmethod
    def display_exercise_by_id(exerciseID):
        select_exerciseQuery = ("SELECT * FROM exercises where exercisesID=%s" % exerciseID)
        result = dbManager.fetch(select_exerciseQuery)

    @staticmethod
    def delete_exercise_by_id(exerciseID):
        delete_query = "DELETE FROM exercises where exercisesID=%s" % exerciseID
        return dbManager.commit(delete_query)

   # @staticmethod
    #def dexercise_details(userEmail,exercisesID,exercise_id,fromTime,toTime,dayOfWeek,name,address):
     #   exercises_query = ("SELECT  e.*,count(s.userEmail) as participants FROM exercises e"
      #                 " LEFT JOIN signedExerciseUsers s on e.exercisesID = s.exercise_id"
       #                " GROUP BY e.exercisesID,e.fromTime,e.toTime,e.dayOfWeek,e.name,e.address;")
        #result = dbManager.fetch(exercises_query)
        #return result

    @staticmethod
    def delete_exercise_by_id(exerciseID):
        selectedExercise =("SELECT * FROM exercises e where e.exercisesID='%s'" %
                        id)
        result = dbManager.fetch(selectedExercise)
        return result