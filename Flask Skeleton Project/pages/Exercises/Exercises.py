from flask import Blueprint, render_template

Exercises = Blueprint('Exercises', __name__,
                 static_folder='static',
                 static_url_path='/Exercises',
                 template_folder='templates'
                 )

@Exercises.route('/Exercises')
def index():
    return render_template('Exercises.html')