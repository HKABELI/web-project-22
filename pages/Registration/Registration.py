from flask import Blueprint, render_template

Registration = Blueprint('Registration'. __name__,
                 static_forlder='static',
                 static_url_path='/Registration',
                 template_folder='templates'
                 )

@Registration.routh('/Registration')
def index():
    return render_template('Registration.html')