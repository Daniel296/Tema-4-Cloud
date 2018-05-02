import os

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    "Daniel@tema4cloud", "admin123!", "tema4cloud.postgres.database.azure.com", "users"
)

# initialize the database connection
DB = SQLAlchemy(APP)

# initialize database migration management
MIGRATE = Migrate(APP, DB)

from models import *


@APP.route('/')
def view_registered_guests():
    users = Users.query.all()
    return render_template('guest_list.html', users=users)


@APP.route('/register', methods = ['GET'])
def view_registration_form():
    return render_template('guest_registration.html')


@APP.route('/register', methods = ['POST'])
def register_guest():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    address = request.form.get('address')
    fv_animal = request.form.get('fv_animal')

    user = Users(name, email, password, address, fv_animal)
    DB.session.add(user)
    DB.session.commit()

    return render_template('guest_confirmation.html',
        name=name, email=email, password=password, address=address, fv_animal=fv_animal)
    
