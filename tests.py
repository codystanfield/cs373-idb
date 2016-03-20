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
        self.assertEqual(name,  cocktail.name)
        self.assertEqual(glass,  cocktail.glass)
        self.assertEqual(recipe,  cocktail.recipe)
        self.assertEqual(None,  cocktail.image)

    def test_cocktail_init_2 (self) :
        name    = "Vodka Sprite"
        glass   = "Glass"
        recipe  = "Vodka Sprite Recipe"
        cocktail = Cocktail(self, name, glass, recipe)
        self.assertEqual(name,  cocktail.name)
        self.assertEqual(glass,  cocktail.glass)
        self.assertEqual(recipe,  cocktail.recipe)
        self.assertEqual(None,  cocktail.image)

    def test_cocktail_init_3 (self) :
        name    = "Vodka Sprite"
        glass   = "Glass"
        recipe  = "Vodka Sprite Recipe"
        cocktail = Cocktail(self, name, glass, recipe)
        self.assertEqual(name,  cocktail.name)
        self.assertEqual(glass,  cocktail.glass)
        self.assertEqual(recipe,  cocktail.recipe)
        self.assertEqual(None,  cocktail.image)

    # ----------
    # cocktail__repr__
    # ----------

    def test_cocktail_repr_1(self) :
        name    = "Vodka Sprite"
        glass   = "Glass"
        recipe  = "Vodka Sprite Recipe"
        cocktail = Cocktail(self, name, glass, recipe)
        drink = cocktail.__repr__(self)
        self.assertEqual("<Cocktail Vodka Sprite>", drink)

    def test_cocktail_repr_2 (self) :
        name    = "Vodka Sprite"
        glass   = "Glass"
        recipe  = "Vodka Sprite Recipe"
        cocktail = Cocktail(self, name, glass, recipe)
        drink = cocktail.__repr__(self)
        self.assertEqual("<Cocktail Vodka Sprite>", drink)

    def test_cocktail_repr_3 (self) :
        name    = "Vodka Sprite"
        glass   = "Glass"
        recipe  = "Vodka Sprite Recipe"
        cocktail = Cocktail(self, name, glass, recipe)
        drink = cocktail.__repr__(self)
        self.assertEqual("<Cocktail Vodka Sprite>", drink)

    # ----------
    # ingredient__init__
    # ----------

    def test_ingredient_init_1(self) :
        name    = "Vodka Sprite"
        ingredient = Ingredient(self, name)
        self.assertEqual(name,  ingredient.name)
        self.assertEqual(None,  ingredient.amount)
        self.assertEqual(None,  ingredient.image)

    def test_ingredient_init_2 (self) :
        name    = "Vodka Sprite"
        ingredient = Ingredient(self, name)
        self.assertEqual(name,  ingredient.name)
        self.assertEqual(None,  ingredient.amount)
        self.assertEqual(None,  ingredient.image)

    def test_ingredient_init_3 (self) :
        name    = "Vodka Sprite"
        ingredient = Ingredient(self, name)
        self.assertEqual(name,  ingredient.name)
        self.assertEqual(None,  ingredient.amount)
        self.assertEqual(None,  ingredient.image)

    # ----------
    # ingredient__repr__
    # ----------

    def test_ingredient_repr_1(self) :
        name    = "Vodka Sprite"
        ingredient = Ingredient(self, name)
        ingredientName = ingredient.__repr__(self)
        self.assertEqual("<Ingredient Vodka Sprite>", ingredientName)

    def test_ingredient_repr_2 (self) :
        name    = "Vodka Sprite"
        ingredient = Ingredient(self, name)
        ingredientName = ingredient.__repr__(self)
        self.assertEqual("<Ingredient Vodka Sprite>", ingredientName)

    def test_ingredient_repr_3 (self) :
        name    = "Vodka Sprite"
        ingredient = Ingredient(self, name)
        ingredientName = ingredient.__repr__(self)
        self.assertEqual("<Ingredient Vodka Sprite>", ingredientName)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
