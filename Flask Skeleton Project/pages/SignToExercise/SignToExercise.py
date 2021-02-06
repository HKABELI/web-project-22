from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
import mysql.connector

SignToExercise = Blueprint('SignToExercise', __name__,
                  static_folder='static',
                  static_url_path='/SignToExercise',
                  template_folder='templates'
                  )

@SignToExercise.route('/SignToExercise',methods=['GET', 'POST'])
def SignToExercise1():
    if request.method == "POST":
        insertNewAppointementQuery = "INSERT INTO signedExerciseUsers (exercise_id,userEmail) values(%s,'%s')" % (
        request.form["exerciseID"],  session.get("userEmail"))
        print(insertNewAppointementQuery)
        query1 = dbManager.commit(insertNewAppointementQuery)
        if(query1):
            return redirect(url_for('Exercises.index'))
        else:
            return render_template("SignToExercise.html", message="something when wrong please contact administrator")
    else:
        selectedExercise = ("SELECT * FROM exercises e where e.exercisesID='%s'" %
                            request.args.get("id"))
        result= dbManager.fetch(selectedExercise)
        return  render_template('SignToExercise.html', exercise = result)