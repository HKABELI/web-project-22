from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
import mysql.connector

createExercise = Blueprint('createExercise', __name__,
                           static_folder='static',
                           static_url_path='/createExercise',
                           template_folder='templates'
                           )


@createExercise.route('/createExercise', methods=['GET', 'POST'])
def createExercise1():
    if request.method == "POST":
        insert_exercise_query = ("INSERT INTO exercises (name,fromTime,"
                                 " toTime,dayOfWeek,capacity,address) VALUES ("
                                 "'%s','%s','%s',%s,%s,'%s')" %
                                 (request.form["name"], request.form["fromTime"], request.form["toTime"],
                                  request.form["dayOfWeek"], request.form["capacity"], request.form["address"]))
        result = dbManager.commit(insert_exercise_query)
        if (result):
            return redirect(url_for('Admin.Admin1'))
    else:
        return render_template('createExercise.html')


@createExercise.route('/editExercise', methods=['GET', 'POST'])


def editExercise():
    if request.method == "POST":
        update_exercise_query = ("UPDATE exercises  SET name='%s',"
                                 "fromTime='%s',"
                                 " toTime='%s',"
                                 "dayOfWeek=%s,"
                                 "capacity=%s,"
                                 "address='%s' WHERE exercisesID=%s" %
                                 (request.form["name"], request.form["fromTime"], request.form["toTime"],
                                  request.form["dayOfWeek"], request.form["capacity"], request.form["address"],
                                  request.form["exerciseID"]))
        result = dbManager.commit(update_exercise_query)
        if (result):
            return redirect(url_for('Admin.Admin1'))
    else:
        exerciseID = request.args.get("id")
        select_exerciseQuery = ("SELECT * FROM exercises where exercisesID=%s" % exerciseID)
        result = dbManager.fetch(select_exerciseQuery)
        return render_template('createExercise.html', exercise=result)


@createExercise.route('/deleteExercise', methods=['GET', 'POST'])


def deleteExercise():
    exerciseID = request.args.get("id")
    if (exerciseID):
        delete_query = "DELETE FROM exercises where exercisesID=%s" % exerciseID
        result = dbManager.commit(delete_query)
    return redirect(url_for('Admin.Admin1'))
