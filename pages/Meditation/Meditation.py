from flask import Blueprint, render_template

Meditation = Blueprint('Meditation'. __name__,
                 static_forlder='static',
                 static_url_path='/Meditation',
                 template_folder='templates'
                 )

@Meditation.routh('/Meditation')
def index():
    return render_template('Meditation.html')