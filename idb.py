# imports
import psycopg2
from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from database import SQLALCHEMY_DATABASE_URI
from database import db_session


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


# remove database sessions at the end of the request or when the application
# shuts down:
# http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/cocktails")
def render_cocktails():
  return render_template('index.html')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#   return render_template('index.html')

# @app.route('/partials/<path:path>')
# def serve_partial():
#   return render_template('/partials/{}'.format(path))

# @app.route('/', defaults={'path': ''}, methods=['GET'])
# @app.route('/<path:path>')
# def catch_all(path):
#   return render_template('index.html')


if __name__ == '__main__':
  app.run()
