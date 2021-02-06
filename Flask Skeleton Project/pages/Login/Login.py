from flask import Blueprint, render_template

Login = Blueprint('Login', __name__,
                 static_folder='static',
                 static_url_path='/Login',
                 template_folder='templates'
                 )

@Login.route('/Login')
def index():
    return render_template('LoginPage.html')


