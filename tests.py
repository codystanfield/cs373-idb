#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from models import Cocktail, Ingredient

# -----------
# TestNetflix
# -----------

class TestIdb (TestCase) :

    # ----------
    # cocktail__init__
    # ----------

    def test_cocktail_init_1(self) :
        name    = "Vodka Sprite"
        glass   = "Glass"
        recipe  = "Vodka Sprite Recipe"
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_2 (self) :
        name    = "Moscow Mule"
        glass   = "Cup"
        recipe  = "Moscow Mule Recipe"
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_3 (self) :
        name    = "Bloody Mary"
        glass   = "Flute"
        recipe  = "Bloody Mary Recipe"
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    # ----------
    # cocktail__repr__
    # ----------

    def test_cocktail_repr_1(self) :
        cocktail = Cocktail("Vodka Sprite", "Glass", "Vodka Sprite Recipe")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail 'Vodka Sprite'>", drink)

    def test_cocktail_repr_2 (self) :
        cocktail = Cocktail("Moscow Mule", "Cup", "Moscow Mule Recipe")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail 'Moscow Mule'>", drink)

    def test_cocktail_repr_3 (self) :
        cocktail = Cocktail("Bloody Mary", "Flute", "Bloody Mary Recipe")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail 'Bloody Mary'>", drink)

    # ----------
    # ingredient__init__
    # ----------

    def test_ingredient_init_1(self) :
        name    = "Rum"
        ingredient = Ingredient(name)
        self.assertEqual(name,  ingredient.name)
        self.assertEqual(None,  ingredient.image)

    def test_ingredient_init_2 (self) :
        name    = "Lime"
        ingredient = Ingredient(name)
        self.assertEqual(name,  ingredient.name)
        self.assertEqual(None,  ingredient.image)

    def test_ingredient_init_3 (self) :
        name    = "Ice"
        ingredient = Ingredient(name)
        self.assertEqual(name,  ingredient.name)
        self.assertEqual(None,  ingredient.image)

    # ----------
    # ingredient__repr__
    # ----------

    def test_ingredient_repr_1(self) :
        name    = "Rum"
        ingredient = Ingredient(name)
        ingredientName = ingredient.__repr__()
        self.assertEqual("<Ingredient 'Rum'>", ingredientName)

    def test_ingredient_repr_2 (self) :
        name    = "Lime"
        ingredient = Ingredient(name)
        ingredientName = ingredient.__repr__()
        self.assertEqual("<Ingredient 'Lime'>", ingredientName)

    def test_ingredient_repr_3 (self) :
        name    = "Ice"
        ingredient = Ingredient(name)
        ingredientName = ingredient.__repr__()
        self.assertEqual("<Ingredient 'Ice'>", ingredientName)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
