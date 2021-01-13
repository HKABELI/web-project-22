from flask import Blueprint, render_template

Asana = Blueprint('Asana'. __name__,
                 static_forlder='static',
                 static_url_path='/Asana',
                 template_folder='templates'
                 )

@Asana.routh('/Asana')
def index():
    return render_template('Asana.html')