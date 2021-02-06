from flask import render_template, Blueprint, request, redirect
from utilities.db.db_manager import dbManager

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
        exist_query = "SELECT email AS count FROM users WHERE email = '%s'  AND first_name = '%s' AND  phone_number = '%s' " % (
            email, first_name, phone_number)
        result = dbManager.fetch(exist_query)
        if len(result) > 0:
            #if user in the user list
            query = "INSERT INTO contact_us(email,first_name,phone_number,message) VALUES ('%s','%s','%s','%s')" % (
                email, first_name, phone_number, message)
            dbManager.commit(query)
            return render_template('Contactus.html', email=email, status='success')
        elif email == '':
            return render_template('Contactus.html', email=email, status='no details')
        else:
            return render_template('Contactus.html', email=email, status='incorrect details')
    else:
        return render_template('Contactus.html')
