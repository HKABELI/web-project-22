from flask import Blueprint, render_template

Pranayama = Blueprint('Pranayama'. __name__,
                 static_forlder='static',
                 static_url_path='/Pranayama',
                 template_folder='templates'
                 )

@Pranayama.routh('/Pranayama')
def index():
    return render_template('Pranayama.html')