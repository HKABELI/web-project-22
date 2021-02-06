from flask import render_template, Blueprint, request, redirect, url_for
from utilities.db.classes.contact_us_db import ContactUsDb
import json


message_from_users = Blueprint('message_from_users', __name__,
                               static_folder='static',
                               static_url_path='/message_from_users',
                               template_folder='templates'
                               )

month_filter = None


@message_from_users.route('/message_from_users')
def message():
        query_result = ContactUsDb.get_all_messages()
        return render_template('message_from_users.html', contact_us=query_result)


@message_from_users.route('/delete_message', methods=['GET', 'POST'])
def delete_message():
    if request.method == 'GET':
        email = request.args['email']
        ContactUsDb.delete_message_by_email(email)
    return redirect('/message_from_users')


@message_from_users.route('/month_message')
def month_message():
    month = request.args['month']
    month_filter = ContactUsDb.get_all_messages_in_month(month)
    return render_template('message_from_users.html', contact_us_month=month_filter)




