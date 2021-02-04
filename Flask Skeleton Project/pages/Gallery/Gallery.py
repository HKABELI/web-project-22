from flask import Blueprint, render_template

Gallery = Blueprint('Gallery', __name__,
                 static_folder='static',
                 static_url_path='/Gallery',
                 template_folder='templates'
                 )

@Gallery.route('/Gallery')
def index():
    return render_template('GalleryPage.html')