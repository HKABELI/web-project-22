from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
import mysql.connector

Exercises = Blueprint('Exercises', __name__,
                 static_folder='static',
                 static_url_path='/Exercises',
                 template_folder='templates'
                 )

# @Exercises.route('/Exercises')
# def index():
#     return render_template('Exercises.html')

@Exercises.route('/Exercises')
def index():
    exercises_query = ("SELECT  e.*,count(s.userEmail) as participants FROM exercises e"
                       " LEFT JOIN signedExerciseUsers s on e.exercisesID = s.exercise_id"
                       " GROUP BY e.exercisesID,e.fromTime,e.toTime,e.dayOfWeek,e.name,e.address;")
    result = dbManager.fetch(exercises_query)
    exercises = {}
    for row in result:
        if not row.dayOfWeek in exercises:
            exercises[row.dayOfWeek] = []
        exercises[row.dayOfWeek].append(row)
    print(exercises)
    myExercisesQuery = ("SELECT s.exercise_id FROM signedExerciseUsers s where s.userEmail='%s'" %
                        session.get("userEmail"))
    myExercisesResults = dbManager.fetch(myExercisesQuery,)
    myExercises = []
    for exercise in myExercisesResults:
        myExercises.append(exercise.exercise_id)

    print(myExercises)
    return render_template('Exercises.html', exercises=exercises,myExercises = myExercises)