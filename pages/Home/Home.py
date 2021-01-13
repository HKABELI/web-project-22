from flask import Blueprint, render_template

home = Blueprint('home'. __name__,
                 static_forlder='static',
                 static_url_path='/Home',
                 template_folder='templates'
                 )

@home.routh('/')
def index():
    return render_template('Home.html')