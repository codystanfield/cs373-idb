#!/usr/bin/env python3

# -------
# imports
# -------

from unittest import main, \
                     TestCase
from models import Cocktail, \
                   Ingredient, \
                   Amount
import requests
import idb

HOST = 'http://104.130.22.54'
# HOST = 'http://localhost:5000'

# -----------
# TestIDB
#  Total of 125 tests written
# -----------

class TestIdb(TestCase):
    """Unit tests for methods in models.py and idb.py"""

    # ----------
    # cocktail__init__
    # ----------

    def test_cocktail_init_1(self):
        """Test __init__ method for the class Cocktail"""
        name = "Vodka Sprite"
        glass = "Glass"
        recipe = "Vodka Sprite Recipe"
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_2(self):
        """Test __init__ method for the class Cocktail"""
        cocktail = Cocktail(None, None, None)
        self.assertEqual(None, cocktail.name)
        self.assertEqual(None, cocktail.glass)
        self.assertEqual(None, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_3(self):
        """Test __init__ method for the class Cocktail"""
        name = ""
        glass = ""
        recipe = ""
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_4(self):
        """Test __init__ method for the class Cocktail"""
        name = "Aqua"
        glass = "Bottle"
        recipe = "Aqua Recipe"
        image = "static/images/cocktails/Aqua.jpg"
        cocktail = Cocktail(name, glass, recipe, image)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(image, cocktail.image)

    def test_cocktail_init_5(self):
        """Test __init__ method for the class Cocktail"""
        name = "Aqua"
        glass = "Bottle"
        recipe = "Aqua Recipe"
        image = "static/images/cocktails/Aqua.jpg"
        cocktail = Cocktail(name, glass, recipe, image)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertIsNotNone(cocktail.image)

    def test_cocktail_init_6(self):
        """Test __init__ method for the class Cocktail"""
        name = None
        glass = None
        recipe = None
        image = "static/images/cocktails/Aqua.jpg"
        cocktail = Cocktail(name, glass, recipe, image)
        self.assertIsNone(cocktail.name)
        self.assertIsNone(cocktail.glass)
        self.assertIsNone(cocktail.recipe)
        self.assertIsNotNone(cocktail.image)

    def test_cocktail_init_7(self):
        """Test __init__ method for the class Cocktail"""
        name = "None"
        glass = "None"
        recipe = "None"
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    # ----------
    # cocktail__repr__
    # ----------

    def test_cocktail_repr_1(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail("Vodka Sprite", "Glass", "Vodka Sprite Recipe")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail '%s'>" % cocktail.name, drink)

    def test_cocktail_repr_2(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail(None, None, None, None)
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail None>", drink)

    def test_cocktail_repr_3(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail("", "", "")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail ''>", drink)

    def test_cocktail_repr_4(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail '%s'>" % cocktail.name, drink)

    # ----------
    # ingredient__init__
    # ----------

    def test_ingredient_init_1(self):
        """Test __init__ method for the class Ingredient"""
        name = "Rum"
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    def test_ingredient_init_2(self):
        """Test __init__ method for the class Ingredient"""
        name = None
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    def test_ingredient_init_3(self):
        """Test __init__ method for the class Ingredient"""
        name = ""
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    def test_ingredient_init_4(self):
        """Test __init__ method for the class Ingredient"""
        name = "Berries"
        image = "static/images/ingredients/Berries.jpg"
        ingredient = Ingredient(name, image)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(image, ingredient.image)

    def test_ingredient_init_5(self):
        """Test __init__ method for the class Ingredient"""
        name = "Berries"
        image = "static/images/ingredients/Berries.jpg"
        ingredient = Ingredient(name, image)
        self.assertEqual(name, ingredient.name)
        self.assertIsNotNone(ingredient.image)

    def test_ingredient_init_6(self):
        """Test __init__ method for the class Ingredient"""
        name = None
        image = "static/images/ingredients/Aqua.jpg"
        ingredient = Ingredient(name, image)
        self.assertIsNone(ingredient.name)
        self.assertIsNotNone(ingredient.image)

    def test_ingredient_init_7(self):
        """Test __init__ method for the class Ingredient"""
        name = "None"
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    # ----------
    # ingredient__repr__
    # ----------

    def test_ingredient_repr_1(self):
        """Test __repr__ method for the class Ingredient"""
        name = "Rum"
        ingredient = Ingredient(name)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient '%s'>" % ingredient.name, ingredient_name)

    def test_ingredient_repr_2(self):
        """Test __repr__ method for the class Ingredient"""
        name = None
        ingredient = Ingredient(name)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient None>", ingredient_name)

    def test_ingredient_repr_3(self):
        """Test __repr__ method for the class Ingredient"""
        name = ""
        ingredient = Ingredient(name)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient ''>", ingredient_name)

    def test_ingredient_repr_4(self):
        """Test __repr__ method for the class Ingredient"""
        name = "Berries"
        image = "static/images/ingredients/Berries.jpg"
        ingredient = Ingredient(name, image)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient '%s'>" % ingredient.name, ingredient_name)

# ----------
# amount__init__
# ----------

    def test_amount_init_1(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("Moscow Mule", "Cup", "Moscow Mule Recipe")
        ingredient = Ingredient("Rum")
        amount = "2 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_2(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, None)
        ingredient = Ingredient(None, None)
        amount = "1"
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_3(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("", "", "")
        ingredient = Ingredient("")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_4(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient("Berries", "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_5(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient("Berries", "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(cocktail, value.c_data)
        self.assertIsNotNone(ingredient, value.i_data)
        self.assertIsNotNone(amount, value.amount)

    def test_amount_init_6(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient(None, "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(value.c_data)
        self.assertIsNotNone(value.i_data)
        self.assertIsNotNone(value.amount)

    def test_amount_init_7(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, None)
        ingredient = Ingredient(None, "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(value.c_data)
        self.assertIsNotNone(value.i_data)
        self.assertIsNotNone(value.amount)

    def test_amount_init_8(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient(None, None)
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(value.c_data)
        self.assertIsNotNone(value.i_data)
        self.assertIsNotNone(value.amount)

    # ----------
    # amount__repr__
    # ----------

    def test_amount_repr_1(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail("Moscow Mule", "Cup", "Moscow Mule Recipe")
        ingredient = Ingredient("Rum")
        amount = Amount(cocktail, ingredient, "2 oz.")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    def test_amount_repr_2(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, None)
        ingredient = Ingredient(None, None)
        amount = Amount(cocktail, ingredient, "1")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    def test_amount_repr_3(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail("", "", "")
        ingredient = Ingredient("")
        amount = Amount(cocktail, ingredient, "3 oz.")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    def test_amount_repr_4(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient("Berries", "static/images/ingredients/Berries.jpg")
        amount = Amount(cocktail, ingredient, "3 oz.")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    # ---
    # API
    # ---

    # ---
    # api_cocktail_list
    # ---

    # r = app.app.test_client().get('/api/v1.0/cuisines')
    #     c = r.headers['content-type']
    #     self.assertEqual(c, 'application/json')
    #     j = json.loads(r.data)
    #
    #     self.assertEqual(j['status'], 'success')
    #     # Test Content
    #     self.assertEqual(j['data']['cuisines'][0]['name'], 'Japanese')
    #     self.assertEqual(j['data']['cuisines'][9]['name'], 'Persian')

    # ---
    # api_cocktail_list
    # ---

    def test_api_cocktail_list_1(self):
        result = idb.api_cocktail_list()
        self.assertEqual(result[0], '[')

    def test_api_cocktail_list_2(self):
        result = idb.api_cocktail_list()
        self.assertEqual(result[1], '{')

    def test_api_cocktail_list_3(self):
        result = idb.api_cocktail_list()
        self.assertIsNotNone(result[1])

    # ---
    # api_cocktail
    # ---

    def test_api_cocktail_1(self):
        result = idb.api_cocktail(1)
        self.assertEqual(result[0], '[')

    def test_api_cocktail_2(self):
        result = idb.api_cocktail(1)
        self.assertEqual(result[1], '{')

    def test_api_cocktail_3(self):
        result = idb.api_cocktail(2)
        self.assertEqual(result[1], '{')


    # ---
    # api_cocktail_name
    # ---

    def test_api_cocktail_name_1(self):
        result = idb.api_cocktail_name(1)
        self.assertEqual(result[0], '{')

    def test_api_cocktail_name_2(self):
        result = idb.api_cocktail_name(1)
        self.assertEqual(result[1], '"')

    def test_api_cocktail_name_3(self):
        result = idb.api_cocktail_name(2)
        self.assertEqual(result[1], '"')

    # ---
    # api_cocktail_ingredients
    # ---

    def test_api_cocktail_ingredients_1(self):
        result = idb.api_cocktail_ingredients(1)
        self.assertEqual(result[0], '[')

    def test_api_cocktail_ingredients_2(self):
        result = idb.api_cocktail_ingredients(1)
        self.assertEqual(result[1], '{')

    def test_api_cocktail_ingredients_3(self):
        result = idb.api_cocktail_ingredients(None)
        self.assertEqual(result[1], ']')

    # ---
    # api_cocktail_glass
    # ---

    def test_api_cocktail_glass_1(self):
        result = idb.api_cocktail_glass(1)
        self.assertEqual(result[0], '{')

    def test_api_cocktail_glass_2(self):
        result = idb.api_cocktail_glass(1)
        self.assertEqual(result[1], '"')

    def test_api_cocktail_glass_3(self):
        result = idb.api_cocktail_glass(2)
        self.assertEqual(result[1], '"')

    # ---
    # api_cocktail_recipe
    # ---

    def test_api_cocktail_recipe_1(self):
        result = idb.api_cocktail_recipe(1)
        self.assertEqual(result[0], '{')

    def test_api_cocktail_recipe_2(self):
        result = idb.api_cocktail_recipe(1)
        self.assertEqual(result[1], '"')

    def test_api_cocktail_recipe_3(self):
        result = idb.api_cocktail_recipe(2)
        self.assertEqual(result[1], '"')

    # ---
    # api_cocktail_image
    # ---

    def test_api_cocktail_image_1(self):
        result = idb.api_cocktail_image(1)
        self.assertEqual(result[0], '{')

    def test_api_cocktail_image_2(self):
        result = idb.api_cocktail_image(1)
        self.assertEqual(result[1], '"')

    def test_api_cocktail_image_3(self):
        result = idb.api_cocktail_image(2)
        self.assertEqual(result[1], '"')

    # ---
    # api_ingredient_list
    # ---

    def test_api_ingredient_list_1(self):
        result = idb.api_ingredient_list()
        self.assertEqual(result[0], '[')

    def test_api_ingredient_list_2(self):
        result = idb.api_ingredient_list()
        self.assertEqual(result[1], '{')

    def test_api_ingredient_list_3(self):
        result = idb.api_ingredient_list()
        self.assertIsNotNone(result[1])

    ## ---
    # api_ingredient
    # ---

    def test_api_ingredient_1(self):
        result = idb.api_ingredient(1)
        self.assertEqual(result[0], '[')

    def test_api_ingredient_2(self):
        result = idb.api_ingredient(1)
        self.assertEqual(result[1], '{')

    def test_api_ingredient_3(self):
        result = idb.api_ingredient(2)
        self.assertEqual(result[1], '{')

    # ---
    # api_ingredient_name
    # ---

    def test_api_ingredient_name_1(self):
        result = idb.api_ingredient_name(1)
        self.assertEqual(result[0], '{')

    def test_api_ingredient_name_2(self):
        result = idb.api_ingredient_name(1)
        self.assertEqual(result[1], '"')

    def test_api_ingredient_name_3(self):
        result = idb.api_ingredient_name(2)
        self.assertEqual(result[1], '"')

    # ---
    # api_ingredient_cocktails
    # ---

    def test_api_ingredient_cocktails_1(self):
        result = idb.api_ingredient_cocktails(1)
        self.assertEqual(result[0], '[')

    def test_api_ingredient_cocktails_2(self):
        result = idb.api_ingredient_cocktails(1)
        self.assertEqual(result[1], '{')

    def test_api_ingredient_cocktails_3(self):
        result = idb.api_ingredient_cocktails(None)
        self.assertEqual(result[1], ']')

    # ---
    # api_ingredient_image
    # ---

    def test_api_ingredient_image_1(self):
        result = idb.api_ingredient_image(1)
        self.assertEqual(result[0], '{')

    def test_api_ingredient_image_2(self):
        result = idb.api_ingredient_image(1)
        self.assertEqual(result[1], '"')

    def test_api_ingredient_image_3(self):
        result = idb.api_ingredient_image(2)
        self.assertEqual(result[1], '"')

    # ---
    # api_ingredient_numcocktails
    # ---

    def test_api_ingred_numcocktails_1(self):
        result = idb.api_ingredient_numcocktails(1)
        self.assertEqual(result[0], '{')

    def test_api_ingred_numcocktails_2(self):
        result = idb.api_ingredient_numcocktails(1)
        self.assertEqual(result[1], '"')

    def test_api_ingred_numcocktails_3(self):
        result = idb.api_ingredient_numcocktails(2)
        self.assertEqual(result[1], '"')

# ----
# main
# ----

if __name__ == "__main__":
    main()
