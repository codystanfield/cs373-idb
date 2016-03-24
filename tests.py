#!/usr/bin/env python3

# -------
# imports
# -------

from unittest import main, TestCase

from models import Cocktail, Ingredient, Amount

import requests

import idb

# -----------
# TestIDB
# -----------

class TestIdb(TestCase):
    """Unit tests for methods in models.py"""

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

    def test_api_cocktail_list(self):
        result = idb.api_cocktail_list()
        self.assertEqual(result[0], '')
        self.assertEqual(result[1], 501)
    
    # .....
    
    def test_api_cocktail_route(self):
        res = requests.get('http://localhost:5000/api/cocktail')
        self.assertEqual(res.status_code, 501)
        res = requests.put('http://localhost:5000/api/cocktail')
        self.assertEqual(res.status_code, 405)

# ----
# main
# ----

if __name__ == "__main__":
    main()
