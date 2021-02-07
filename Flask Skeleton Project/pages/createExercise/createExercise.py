from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
from utilities.db.classes.exercises import EXdb
import mysql.connector

createExercise = Blueprint('createExercise', __name__,
                           static_folder='static',
                           static_url_path='/createExercise',
                           template_folder='templates'
                           )


@createExercise.route('/createExercise', methods=['GET', 'POST'])
def createExercise1():
    if request.method == "POST":
        name = request.form['name']
        fromTime = request.form['fromTime']
        toTime = request.form['toTime']
        dayOfWeek = request.form['dayOfWeek']
        capacity = request.form['capacity']
        address = request.form['address']
        result = EXdb.add_exercises(name, fromTime, toTime, dayOfWeek, capacity, address)
        if (result):
            return redirect(url_for('Admin.Admin1'))
    else:
        return render_template('createExercise.html')


# @createExercise.route('/editExercise', methods=['GET', 'POST'])
# def editExercise():
#     if request.method == "POST":
#         name = request.form['name']
#         fromTime = request.form['fromTime']
#         toTime = request.form['toTime']
#         dayOfWeek = request.form['dayOfWeek']
#         capacity = request.form['capacity']
#         address = request.form['address']
#         result = EXdb.edit_exercises(name, fromTime, toTime, dayOfWeek, capacity, address)
#         if (result):
#             return redirect(url_for('Admin.Admin1'))
#     else:
#         exerciseID = request.args.get("id")
#         result= EXdb.display_exercise_by_id(exerciseID)
#         return render_template('createExercise.html', exercise=result)



@createExercise.route('/editExercise', methods=['GET', 'POST'])
def editExercise():
    if request.method == "POST":
        update_exercise_query = ("UPDATE exercises  SET name='%s',"
                                 "fromTime='%s',"
                                 " toTime='%s',"
                                 "dayOfWeek=%s,"
                                 "capacity=%s,"
                                 "address='%s' WHERE exercisesID=%s" %
                                 (request.form["name"],request.form["fromTime"],request.form["toTime"],
                                  request.form["dayOfWeek"],request.form["capacity"],request.form["address"],
                                  request.form["exerciseID"]))

       # result = interact_db(update_exercise_query, query_type='commit')
        result = dbManager.commit(update_exercise_query)
        if(result):
            return redirect(url_for('Admin.Admin1'))
        else:
            return render_template('createExercise.html')
    else:
        exerciseID = request.args.get("id")
        select_exerciseQuery = ("SELECT * FROM exercises where exercisesID=%s" % exerciseID)
        result = dbManager.fetch(select_exerciseQuery)
      #  result = interact_db(select_exerciseQuery,query_type="fetch")
        return render_template('createExercise.html',exercise=result)





@createExercise.route('/deleteExercise', methods=['GET', 'POST'])
def deleteExercise():
    if request.method == 'GET':
        exerciseID = request.args.get("id")
        EXdb.delete_exercise_by_id(exerciseID)
    return redirect(url_for('Admin.Admin1'))



