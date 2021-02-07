from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
import mysql.connector
from utilities.db.classes.users_signed_exercises import UsersSigned
from utilities.db.classes.exercises import EXdb

SignToExercise = Blueprint('SignToExercise', __name__,
                           static_folder='static',
                           static_url_path='/SignToExercise',
                           template_folder='templates'
                           )


@SignToExercise.route('/SignToExercise', methods=['GET', 'POST'])
def SignToExercise1():
    if request.method == "POST":
        exerciseID = request.form["exerciseID"]
        userEmail = session.get("userEmail")
        query1= UsersSigned.sign_to_exercise(exerciseID,userEmail)
        if (query1):
            return redirect(url_for('Exercises.index'))
        else:
            return render_template("SignToExercise.html", message="something when wrong please contact administrator")
    else:
        exerciseID=request.args.get("id")
        result=EXdb.delete_exercise_by_id(exerciseID)
        return render_template('SignToExercise.html', exercise=result)
