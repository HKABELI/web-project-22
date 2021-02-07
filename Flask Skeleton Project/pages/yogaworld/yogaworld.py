from flask import Blueprint, render_template

yogaworld = Blueprint('yogaworld', __name__,
                 static_folder='static',
                 static_url_path='/Home',
                 template_folder='templates'
                 )


@yogaworld.route('/')
def index():
     return render_template('yogaworld.html')
