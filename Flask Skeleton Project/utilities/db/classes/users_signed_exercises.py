from utilities.db.db_manager import dbManager


class UsersSigned:

    @staticmethod
    def sign_to_exercise(exercise_id,userEmail):
       insertNewAppointementQuery = "INSERT INTO signedExerciseUsers (exercise_id,userEmail) values(%s,'%s')" % (exercise_id,userEmail)
       print(insertNewAppointementQuery)
       query1 = dbManager.commit(insertNewAppointementQuery)
       return query1



