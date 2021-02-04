from flask import Blueprint, render_template

Pranayama = Blueprint('Pranayama', __name__,
                 static_folder='static',
                 static_url_path='/Pranayama',
                 template_folder='templates'
                 )

@Pranayama.route('/Pranayama')
def index():
    return render_template('pranayama.html')