# flask imports
from flask import request, \
                  session, \
                  g, \
                  redirect, \
                  url_for, \
                  abort, \
                  render_template, \
                  flash

# app configuration imports
from config import app, \
                   manager

# unit test imports
from io import StringIO
from tests import TestIdb
from unittest import TextTestRunner, \
                     makeSuite


import os, json, subprocess

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
def api_ingredient(id):
    return ('', 501)


@app.route('/api/ingredient/<int:id>/name', methods=['GET'])
def api_ingredient_name(id):
    return ('', 501)


@app.route('/api/ingredient/<int:id>/cocktails', methods=['GET'])
def api_ingredient_cocktails(id):
    return ('', 501)


@app.route('/api/ingredient/<int:id>/image', methods=['GET'])
def api_ingredient_image(id):
    return ('', 501)


@app.route('/api/ingredient/<int:id>/numcocktails', methods=['GET'])
def api_ingredient_numcocktails(id):
    return ('', 501)

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
