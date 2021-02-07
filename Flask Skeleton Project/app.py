
from flask import Flask, redirect, url_for, render_template, blueprints, jsonify
from flask import request, session
from datetime import timedelta
import mysql.connector


###### App setup
app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')

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

from pages.SignToExercise.SignToExercise import SignToExercise
app.register_blueprint(SignToExercise)

from pages.createExercise.createExercise import createExercise
app.register_blueprint(createExercise)

from pages.Admin.Admin import Admin
app.register_blueprint(Admin)

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

from pages.message_from_users.message_from_users import message_from_users
app.register_blueprint(message_from_users)

from pages.users.users import users
app.register_blueprint(users)

from pages.yogaworld.yogaworld import yogaworld
app.register_blueprint(yogaworld)

# ## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)


###### Components
# Main menu

from components.header.header import header
app.register_blueprint(header)

from components.footer.footer import footer
app.register_blueprint(footer)