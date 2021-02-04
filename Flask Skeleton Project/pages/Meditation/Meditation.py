from flask import Blueprint, render_template

Meditation = Blueprint('Meditation', __name__,
                 static_folder='static',
                 static_url_path='/Meditation',
                 template_folder='templates'
                 )

@Meditation.route('/Meditation')
def index():
    return render_template('Meditation.html')