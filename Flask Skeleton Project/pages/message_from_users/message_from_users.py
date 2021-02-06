from flask import render_template, Blueprint, request, redirect
from utilities.db.db_manager import dbManager

message_from_users = Blueprint('message_from_users', __name__,
                               static_folder='static',
                               static_url_path='/message_from_users',
                               template_folder='templates'
                               )


@message_from_users.route('/message_from_users')
def message():
    query = "select * from contact_us"
    query_result = dbManager.fetch(query)
    return render_template('message_from_users.html', contact_us=query_result)


@message_from_users.route('/delete_message', methods=['GET', 'POST'])
def delete_message():
    if request.method == 'GET':
        email = request.args['email']
        query = "DELETE FROM  contact_us WHERE email='%s'" % email
        dbManager.commit(query)
    return redirect('/message_from_users')
