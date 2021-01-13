from flask import Blueprint, render_template

Yoga = Blueprint('Yoga'. __name__,
                 static_forlder='static',
                 static_url_path='/Yoga',
                 template_folder='templates'
                 )

@Yoga.routh('/Yoga')
def index():
    return render_template('Yoga.html')