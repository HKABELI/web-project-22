from flask import Flask


###### App setup
app = Flask(__name__)
# app.config.from_pyfile('settings.py')

###### Pages
from pages.Home.Home import Home
app.register_blueprint(Home)

from pages.Aboutme.Aboutme import Aboutme
app.register_blueprint(Aboutme)

from pages.Asana.Asana import Asana
app.register_blueprint(Asana)

from pages.Contactus.Contactus import Contactus
app.register_blueprint(Contactus)

from pages.Exercises.Exercises import Exercises
app.register_blueprint(Exercises)

from pages.Gallery.Gallery import Gallery
app.register_blueprint(Gallery)

from pages.Login.Login import Login
app.register_blueprint(Login)

from pages.Meditation.Meditation import Meditation
app.register_blueprint(Meditation)

from pages.Pranayama.Pranayama import Pranayama
app.register_blueprint(Pranayama)

from pages.Registration.Registration import Registration
app.register_blueprint(Registration)

from pages.Yoga.Yoga import Yoga
app.register_blueprint(Yoga)
# ## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)


###### Components
# Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
