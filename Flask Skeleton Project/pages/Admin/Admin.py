from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request, session
from utilities.db.db_manager import dbManager
import mysql.connector

Admin = Blueprint('Admin', __name__,
                  static_folder='static',
                  static_url_path='/Admin',
                  template_folder='templates'
                  )


@Admin.route('/Admin')
def Admin1():
    exercises_list_query=("SELECT * FROM exercises")
    result = dbManager.fetch(exercises_list_query)

    return render_template("Admin.html", exercises_list=result)
