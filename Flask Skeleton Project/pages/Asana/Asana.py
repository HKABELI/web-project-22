from flask import Blueprint, render_template

Asana = Blueprint('Asana', __name__,
                 static_folder='static',
                 static_url_path='/Asana',
                 template_folder='templates'
                 )

@Asana.route('/Asana')
def index():
    return render_template('Asana.html')