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


@app.route('/cocktails/<int:id>')
def cocktails(id):
    return render_template('index.html', cocktail_id=id)


@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
  

@app.route('/api/cocktail', methods=['GET'])
def api_cocktail_list():
    return ('', 501)
    
    
@app.route('/api/cocktail/<int:id>', methods=['GET'])
def api_cocktail(id):
    return ('', 501)
    
    
@app.route('/api/cocktail/<int:id>/name', methods=['GET'])
def api_cocktail_name(id):
    return ('', 501)

    
@app.route('/api/cocktail/<int:id>/ingredients', methods=['GET'])
def api_cocktail_ingredients(id):
    return ('', 501)
    

@app.route('/api/cocktail/<int:id>/glass', methods=['GET'])
def api_cocktail_glass(id):
    return ('', 501)


@app.route('/api/cocktail/<int:id>/recipe', methods=['GET'])
def api_cocktail_recipe(id):
    return ('', 501)


@app.route('/api/cocktail/<int:id>/image', methods=['GET'])
def api_cocktail_image(id):
    return ('', 501)


@app.route('/api/ingredient', methods=['GET'])
def api_ingredient_list():
    return ('', 501)


@app.route('/api/ingredient/<int:id>', methods=['GET'])
def api_ingredient():
    return ('', 501)


@app.route('/api/ingredient/<int:id>/name', methods=['GET'])
def api_ingredient_name():
    return ('', 501)


@app.route('/api/ingredient/<int:id>/cocktails', methods=['GET'])
def api_ingredient_cocktails():
    return ('', 501)


@app.route('/api/ingredient/<int:id>/image', methods=['GET'])
def api_ingredient_image():
    return ('', 501)


@app.route('/api/ingredient/<int:id>/numcocktails', methods=['GET'])
def api_ingredient_numcocktails():
    return ('', 501)
    

if __name__ == '__main__':
    app.run()
