from flask import render_template, Blueprint

Aboutme = Blueprint('Aboutme', __name__,
                 static_folder='static',
                 static_url_path='/Aboutme',
                 template_folder='templates'
                 )

@Aboutme.route('/Aboutme')
def index():
    return render_template('Aboutme.html')