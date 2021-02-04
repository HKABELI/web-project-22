from flask import Blueprint, render_template

Contactus = Blueprint('Contactus', __name__,
                 static_folder='static',
                 static_url_path='/Contactus',
                 template_folder='templates'
                 )

@Contactus.route('/Contactus')
def contactus():
    return render_template('Contactus.html')