from flask import Blueprint, render_template

Contactus = Blueprint('Contactus'. __name__,
                 static_forlder='static',
                 static_url_path='/Contactus',
                 template_folder='templates'
                 )

@Contactus.routh('/Contactus')
def index():
    return render_template('Contactus.html')