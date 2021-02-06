from flask import render_template, Blueprint, request, redirect
from utilities.db.db_manager import dbManager

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
        exist_query = "SELECT email as count FROM users where email = '%s'" % email
        result = dbManager.fetch(exist_query)
        if len(result) == 0:
            query = "INSERT INTO users(email,first_name,last_name,password,phone_number) VALUES ('%s','%s','%s','%s','%s')" % (
                email, first_name, last_name, password, phone_number)
            dbManager.commit(query)
            return render_template('Registration.html', email=email, status='success')
        elif email == '':
            return render_template('Registration.html', email=email, status='no details')
        else:
            return render_template('Registration.html', email=email, status='incorrect details')
    else:
        return render_template('Registration.html')
