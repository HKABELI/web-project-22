from flask import render_template, Blueprint, request, redirect
from utilities.db.classes.users_db import UsersDb

users = Blueprint('users', __name__,
                 static_folder='static',
                 static_url_path='/users',
                 template_folder='templates'
                 )

@users.route('/users')
def users_list():
    query_result = UsersDb.get_all_users()
    return render_template('users.html', users=query_result)


@users.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        email = request.args['email']
        UsersDb.delete_user_by_email(email)
    return redirect('/users')


