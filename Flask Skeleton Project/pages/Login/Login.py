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

