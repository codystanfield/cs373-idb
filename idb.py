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


def connect_db():
  return SQLAlchemy(app)


# remove database sessions at the end of the request or when the application
# shuts down:
# http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()


# example route and function from here:
# http://flask.pocoo.org/docs/0.10/tutorial/views/
@app.route('/')
def show_entries():
  # cur = g.db.execute('select title, text from entries order by id desc')
  # entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
  return render_template('index.html')#, entries=entries)


if __name__ == '__main__':
  app.run()
