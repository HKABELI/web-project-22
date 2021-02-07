from flask import Blueprint, render_template

yogaworld = Blueprint('yogaworld', __name__,
                 static_folder='static',
                 static_url_path='/yogaworld',
                 template_folder='templates'
                 )


@yogaworld.route('/yogaworld')
def index():
     return render_template('yogaworld.html')
