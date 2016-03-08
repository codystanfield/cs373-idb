
# To use SQLAlchemy in a declarative way with your application, you just have to
# put the following code into your application module. Flask will automatically
# remove database sessions at the end of the request or when the application
# shuts down:
# http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
# from database import db_session
#
# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()

# all the imports
import psycopg2
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
# or load environment variables from file:
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    return psycopg2.connect(app.config['DATABASE'])

def connect_db():

if __name__ == '__main__':
    app.run()
