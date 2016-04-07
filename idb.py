# flask imports
from flask import request, \
                  session, \
                  g, \
                  redirect, \
                  url_for, \
                  abort, \
                  render_template, \
                  flash, \
                  jsonify

# app configuration imports
from config import app, \
                   manager

# unit test imports
from io import StringIO
from models import Cocktail, \
                   Ingredient, \
                   Amount
from tests import TestIdb
from unittest import TextTestRunner, \
                     makeSuite
import json


import os, json, subprocess

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/cocktails/<int:id_>')
def cocktails(id_):
    return render_template('index.html', cocktail_id=id_)


@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@app.route('/api/cocktail', methods=['GET'])
def api_cocktail_list():
    results = []
    for c in Cocktail.query.all():
        results.append({'name': c.name, 'id': c.id_})

    return json.dumps(results)


@app.route('/api/cocktail/<int:id_>', methods=['GET'])
def api_cocktail(id_):
    results = []

    c = Cocktail.query.filter(Cocktail.id_ == id_).one_or_none()
    obj = {}
    obj['id'] = c.id_
    obj['name'] = c.name
    obj['recipe'] = c.recipe
    obj['glass'] = c.glass
    obj['imageURL'] = '/static/images/' + c.image

    ingredients = []

    for i in Amount.query.filter(Amount.cocktail == id_):
        ing = Ingredient.query.filter(Ingredient.id_ == i.ingredient).one_or_none()
        ingredients.append({'name': ing.name, 'quantity': i.amount})
    obj['ingredients'] = ingredients

    results.append(obj)

    return json.dumps(results)


@app.route('/api/cocktail/<int:id_>/name', methods=['GET'])
def api_cocktail_name(id_):
    results = []
    c = Cocktail.query.filter(Cocktail.id_ == id_).one_or_none()
    return json.dumps({'name': c.name})


@app.route('/api/cocktail/<int:id_>/ingredients', methods=['GET'])
def api_cocktail_ingredients(id_):
    results = []
    c = Cocktail.query.filter(Cocktail.id_ == id_).one_or_none()
    
    for i in Amount.query.filter(Amount.cocktail == id_):
        ing = Ingredient.query.filter(Ingredient.id_ == i.ingredient).one_or_none()
        results.append({'name': ing.name, 'quantity': i.amount})
        
    return json.dumps(results)


@app.route('/api/cocktail/<int:id_>/glass', methods=['GET'])
def api_cocktail_glass(id_):
    results = []
    c = Cocktail.query.filter(Cocktail.id_ == id_).one_or_none()
    return json.dumps({'glass': c.glass})


@app.route('/api/cocktail/<int:id_>/recipe', methods=['GET'])
def api_cocktail_recipe(id_):
    results = []
    c = Cocktail.query.filter(Cocktail.id_ == id_).one_or_none()
    return json.dumps({'recipe': c.recipe})


@app.route('/api/cocktail/<int:id_>/image', methods=['GET'])
def api_cocktail_image(id_):
    results = []
    c = Cocktail.query.filter(Cocktail.id_ == id_).one_or_none()
    return json.dumps({'imageURL': '/static/images/{0}'.format(c.image)})


@app.route('/api/ingredient', methods=['GET'])
def api_ingredient_list():
    results = []
    for i in Ingredient.query.all():
        results.append({'name': i.name, 'id': i.id_})

    return json.dumps(results)


@app.route('/api/ingredient/<int:id_>', methods=['GET'])
def api_ingredient(id_):
    results = []
    
    i = Ingredient.query.filter(Ingredient.id_ == id_).one_or_none()
    obj = {}
    obj['id'] = i.id_
    obj['name'] = i.name
    obj['imageURL'] = i.image
    
    cocktails = []
    
    for i in Amount.query.filter(Amount.ingredient == id_):
        c = Cocktail.query.filter(Cocktail.id_ == i.cocktail).one_or_none()
        cocktails.append(c.id_)
        
    obj['cocktails'] = cocktails
    obj['numberOfCocktails'] = len(cocktails)
    
    results.append(obj)
        
    return json.dumps(results)


@app.route('/api/ingredient/<int:id_>/name', methods=['GET'])
def api_ingredient_name(id_):
    results = []
    i = Ingredient.query.filter(Ingredient.id_ == id_).one_or_none()
    return json.dumps({'name': i.name})


@app.route('/api/ingredient/<int:id_>/cocktails', methods=['GET'])
def api_ingredient_cocktails(id_):
    results = []
    i = Ingredient.query.filter(Ingredient.id_ == id_).one_or_none()
    
    for a in Amount.query.filter(Amount.ingredient == id_):
        c = Cocktail.query.filter(Cocktail.id_ == a.cocktail).one_or_none()
        results.append({'name': c.name, 'id': c.id_})
        
    return json.dumps(results)


@app.route('/api/ingredient/<int:id_>/image', methods=['GET'])
def api_ingredient_image(id_):
    results = []
    i = Ingredient.query.filter(Ingredient.id_ == id_).one_or_none()
    return json.dumps({'imageURL': '/static/images/' + i.image})


@app.route('/api/ingredient/<int:id_>/numcocktails', methods=['GET'])
def api_ingredient_numcocktails(id_):
    count = Amount.query.filter(Amount.ingredient == id_).count()
    return json.dumps({'numCocktails': count})

# @app.route('/tests', methods=['GET'])
# def tests():
#     p = subprocess.Popen(["make", "test"],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             stdin=subprocess.PIPE)
#     out, err = p.communicate()
#     return render_template('tests.html', output=err+out)

@app.route('/tests', methods=['GET'])
def tests():
    """
    Runs unit tests and returns the result.
    """
    os.system("make test")
    f = open("TestOutput.tmp", 'r')
    result = []
    for line in f:
        result += [line]
    f.close()
    os.system("make clean")    
    return render_template('tests.html', result=result);

    # p = subprocess.Popen(["make", "test"],
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE,
    #         stdin=subprocess.PIPE)
    # out, err = p.communicate()
    # return render_template('tests.html', output=err+out)
    # io = StringIO()
    # TextTestRunner(stream=io, verbosity=2).run(makeSuite(TestIdb))
    # results = io.getvalue().split('\n')
    # # return results
    # return render_template("tests.html", text=results)

if __name__ == '__main__':
    manager.run()
