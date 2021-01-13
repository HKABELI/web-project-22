from flask import Blueprint, render_template

Login = Blueprint('Login'. __name__,
                 static_forlder='static',
                 static_url_path='/Login',
                 template_folder='templates'
                 )

@Login.routh('/Login')
def index():
    return render_template('Login.html')