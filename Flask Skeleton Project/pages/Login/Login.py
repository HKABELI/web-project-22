from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
from utilities.db.classes.users_db import UsersDb
from utilities.db.classes.user_loggedin import UsersLG

import mysql.connector

Login = Blueprint('Login', __name__,
                  static_folder='static',
                  static_url_path='/Login',
                  template_folder='templates'
                  )


@Login.route('/Login')
def index():
    return render_template('LoginPage.html')


@Login.route('/LoginPage', methods=['GET', 'POST'])
def Login_Page():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        result = UsersDb.is_email_exist_and_password_correct(email, password)
        if len(result) == 0:
            return render_template('LoginPage.html', message="User not exists")
        else:
            session["userEmail"] = email
            session["fullname"] = "  %s %s " % (
                result[0].first_name, result[0].last_name)
        UsersLG.insert_login_user(email)
        return redirect(url_for('Exercises.index'))
    else:
        return render_template('LoginPage.html')
