from flask import render_template, Blueprint, request, redirect
from utilities.db.classes.users_db import UsersDb

Registration = Blueprint('Registration', __name__,
                         static_folder='static',
                         static_url_path='/Registration',
                         template_folder='templates'
                         )


@Registration.route('/Registration')
def index():
    return render_template('Registration.html')


@Registration.route('/Registration', methods=['GET', 'POST'])
def Registrat():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        phone_number = request.form['phone_number']
        # check if user is  not in user list
        result = UsersDb.is_email_exist(email)

        if len(result) == 0:
            UsersDb.insert_user(email, first_name, last_name, password, phone_number)
            return render_template('Home.html', email=email, status='success')
        elif email == '':
            return render_template('Registration.html', email=email, status='no details')
        else:
            return render_template('Registration.html', email=email, status='incorrect details')
    else:
        return render_template('Registration.html')
