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


@app.route('/cocktail')
def cocktail():
  # cur = g.db.execute('select title, text from entries order by id desc')
  # entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
  return render_template('cocktail.html')#, entries=entries)

@app.route('/moscow_mule')
def moscow_mule():
  # cur = g.db.execute('select title, text from entries order by id desc')
  # entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
  return render_template('moscow_mule.html')#, entries=entries)

@app.route('/white_russian')
def white_russian():
  return render_template('white_russian.html')#, entries=entries)

@app.route('/mojito')
def mojito():
  return render_template('mojito.html')#, entries=entries)

@app.route('/ingredients')
def ingredients():
  return render_template('ingredients.html')#, entries=entries)

@app.route('/vodka')
def vodka():
  return render_template('vodka.html')#, entries=entries)

@app.route('/lime_juice')
def lime_juice():
  return render_template('lime_juice.html')#, entries=entries)

@app.route('/ginger_beer')
def ginger_beer():
  return render_template('ginger_beer.html')#, entries=entries)

@app.route('/coffee_liquor')
def coffee_liquor():
  return render_template('coffee_liquor.html')#, entries=entries)

@app.route('/cream')
def cream():
  return render_template('cream.html')#, entries=entries)

@app.route('/rum')
def rum():
  return render_template('rum.html')#, entries=entries)

@app.route('/mint')
def mint():
  return render_template('mint.html')#, entries=entries)

@app.route('/sugar')
def sugar():
  return render_template('sugar.html')#, entries=entries)

@app.route('/soda')
def soda():
  return render_template('soda.html')#, entries=entries)

# example route and function from here:
# http://flask.pocoo.org/docs/0.10/tutorial/views/
@app.route('/')
def index():
  # cur = g.db.execute('select title, text from entries order by id desc')
  # entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
  return render_template('index.html')#, entries=entries)

if __name__ == '__main__':
  app.run()
