from flask import render_template, Blueprint, request, redirect
from utilities.db.classes.contact_us_db import ContactUsDb
from utilities.db.classes.users_db import UsersDb

Contactus = Blueprint('Contactus', __name__,
                      static_folder='static',
                      static_url_path='/Contactus',
                      template_folder='templates'
                      )


@Contactus.route('/Contactus')
def contactus():
    return render_template('Contactus.html')


@Contactus.route('/Contactus', methods=['GET', 'POST'])
def contactus_db():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        phone_number = request.form['phone_number']
        message = request.form['message']
        # check if user is in user list
        result = UsersDb.is_user_exist(email, first_name, phone_number)
        if len(result) > 0:
            # if user in the user list
            ContactUsDb.insert_message(email, first_name, phone_number, message)
            return render_template('Contactus.html', email=email, status='success')
        elif email == '':
            return render_template('Contactus.html', email=email, status='no details')
        else:
            return render_template('Contactus.html', email=email, status='incorrect details')
    else:
        return render_template('Contactus.html')
