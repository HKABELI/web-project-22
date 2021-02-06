from flask import render_template, Blueprint, request, redirect
from utilities.db.db_manager import dbManager

users = Blueprint('users', __name__,
                 static_folder='static',
                 static_url_path='/users',
                 template_folder='templates'
                 )

@users.route('/users')
def users_list():
    query = "select * from users"
    query_result = dbManager.fetch(query)
    return render_template('users.html', users=query_result)


@users.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        email = request.args['email']
        query = "DELETE FROM  users WHERE email='%s'" % email
        dbManager.commit(query)
    return redirect('/users')
