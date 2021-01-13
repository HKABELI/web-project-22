from flask import Blueprint, render_template

Gallery = Blueprint('Gallery'. __name__,
                 static_forlder='static',
                 static_url_path='/Gallery',
                 template_folder='templates'
                 )

@Gallery.routh('/Gallery')
def index():
    return render_template('Gallery.html')