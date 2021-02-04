from flask import Blueprint, render_template

Home = Blueprint('Home', __name__,
                 static_folder='static',
                 static_url_path='/Home',
                 template_folder='templates'
                 )


@Home.route('/')
def index():
     return render_template('Home.html')
