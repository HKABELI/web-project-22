from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
import mysql.connector

Login = Blueprint('Login', __name__,
                  static_folder='static',
                  static_url_path='/Login',
                  template_folder='templates'
                  )


@Login.route('/Login')
def index():
    return render_template('LoginPage.html')


@Login.route('/Login', methods=['GET', 'POST'])
def Login_Page():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        exist_query = "SELECT * FROM users where email = '%s' and password='%s' " % (
            email, password)
        result = dbManager.fetch(exist_query)
        if len(result) == 0:
            return render_template('LoginPage.html', message="User not exists")
        else:
            session["userEmail"] = email
            session["fullname"] = "  %s %s " % (
                result[0].first_name, result[0].last_name)

            insert_loggedin = "INSERT INTO loggedin (email) values('%s')" % (
                email)
            query1 = dbManager.commit(insert_loggedin)
          #  return redirect('/Exercises')
        return redirect(url_for('Exercises.index'))
    else:
        return render_template('LoginPage.html')

###########
[1:08, 7.2.2021] סופיה תעונ: @app.route('/SignToExercise',methods=['GET', 'POST'])
def SignToExercise():
    if request.method == "POST":
        insertNewAppointementQuery = "INSERT INTO signedExerciseUsers (exercise_id,userEmail) values(%s,'%s')" % (
        request.form["exerciseID"],  session.get("userEmail"))
        print(insertNewAppointementQuery)
        query1 = interact_db(insertNewAppointementQuery, query_type='commit')
        if(query1):
            return redirect(url_for('Exercises'))
        else:
            return render_template("SignToExercise.html", message="something when wrong please contact administrator")
    else:
        selectedExercise = ("SELECT * FROM exercises e where e.exercisesID='%s'" %
                            request.args.get("id"))
        resul…
[1:09, 7.2.2021] סופיה תעונ: <!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{ url_for('static',filename='css/styles.css') }}">
    <link rel="stylesheet" href="{{ url_for('static',filename='css/Exercises.css') }}">

    <meta charsey="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="yogaWorld/Asana.html"></script>
    <!---------------script---------------->
    <script src="https://kit.fontawesome.com/6850819008.js" crossorigin="anonymous"></script>
    <script src="static/js/main.js"></script>
    <!------script-->
    <title>הרשמה לשיעור</title>
    <script>
        function seriousnessAlert() {
            alert("בזה הרגע ביצעת רישום לשיעור :) \nסימן שהתחייבת \nהמחויבות הזו היא קודם כל כלפיי עצמך \nואחר כך גם מולי \nבמידה ואתה מעוניין לבטל את השיעור ללא עלות, עלייך לבצע זאת עד 6 שעות לפני שעת תחילת התרגול");
            document.getElementsByTagName("form")[0].submit();
        }
    </script>
</head>
<body>
<Header>     {% include 'Header.html' %} </Header>
{% if(message)!="" %}
<h1 style="color:red;">{{ message }}</h1>
{% endif %}
<div class="confirmation">
    אתה עומד לקבוע שיעור עבור :
    <div class="exercise">
        {% for selectedExercise in exercise %}
            שם השיעור:  {{ selectedExercise.name }} <br/>
             כתובת השיעור: {{ selectedExercise.address }} <br/>
            זמן השיעור: {{ selectedExercise.fromTime  }} to {{ selectedExercise.toTime }}<br/>
            <form action="/SignToExercise" method="post">
                <input type="hidden" name="exerciseID" value="{{ selectedExercise.exercisesID }}">
                <a onclick="seriousnessAlert()" class="Registration">הרשם</a>
            </form>
        {% endfor %}
    </div>
</div>
<Footer>                {% include 'Footer.html' %}        </Footer>
</body>
</html>
#######2####
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{ url_for('static',filename='css/styles.css') }}">
    <link rel="stylesheet" href="{{ url_for('static',filename='css/Exercises.css') }}">

    <meta charsey="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="yogaWorld/Asana.html"></script>
    <!---------------script---------------->
    <script src="https://kit.fontawesome.com/6850819008.js" crossorigin="anonymous"></script>
    <script src="static/js/main.js"></script>
    <!------script-->
    <title>הרשמה לשיעור</title>
    <script>
        function seriousnessAlert() {
            alert("בזה הרגע ביצעת רישום לשיעור :) \nסימן שהתחייבת \nהמחויבות הזו היא קודם כל כלפיי עצמך \nואחר כך גם מולי \nבמידה ואתה מעוניין לבטל את השיעור ללא עלות, עלייך לבצע זאת עד 6 שעות לפני שעת תחילת התרגול");
            document.getElementsByTagName("form")[0].submit();
        }
    </script>
</head>
<body>
<Header>     {% include 'Header.html' %} </Header>
{% if(message)!="" %}
<h1 style="color:red;">{{ message }}</h1>
{% endif %}
<div class="confirmation">
    אתה עומד לקבוע שיעור עבור :
    <div class="exercise">
        {% for selectedExercise in exercise %}
            שם השיעור:  {{ selectedExercise.name }} <br/>
             כתובת השיעור: {{ selectedExercise.address }} <br/>
            זמן השיעור: {{ selectedExercise.fromTime  }} to {{ selectedExercise.toTime }}<br/>
            <form action="/SignToExercise" method="post">
                <input type="hidden" name="exerciseID" value="{{ selectedExercise.exercisesID }}">
                <a onclick="seriousnessAlert()" class="Registration">הרשם</a>
            </form>
        {% endfor %}
    </div>
</div>
<Footer>                {% include 'Footer.html' %}        </Footer>
</body>
</html>