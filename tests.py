#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from models import Cocktail, Ingredient, Amount

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

    def test_cocktail_init_4 (self) :
        name   = "Aqua"
        glass  = "Bottle"
        recipe = "Aqua Recipe"
        image  = "static/images/cocktails/Aqua.jpg"
        cocktail = Cocktail(name, glass, recipe, image)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(image, cocktail.image)

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

    def test_cocktail_repr_4 (self) :
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail '%s'>" % cocktail.name, drink)

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

# ----------
# amount__init__
# ----------

    def test_amount_init_1(self) :
        cocktail = Cocktail("Moscow Mule", "Cup", "Moscow Mule Recipe")
        ingredient = Ingredient("Rum")
        amount      = "2 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail,  value.c_data)
        self.assertEqual(ingredient,  value.i_data)
        self.assertEqual(amount,  value.amount)

    def test_amount_init_2 (self) :
        cocktail = Cocktail("Vodka Sprite", "glass", "Vodka Sprite Recipe")
        ingredient = Ingredient("Lime")
        amount      = "1"
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail,  value.c_data)
        self.assertEqual(ingredient,  value.i_data)
        self.assertEqual(amount,  value.amount)

    def test_amount_init_3 (self) :
        cocktail = Cocktail("Jack and Coke", "cup", "Jack and Coke Recipe")
        ingredient = Ingredient("Coke")
        amount      = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail,  value.c_data)
        self.assertEqual(ingredient,  value.i_data)
        self.assertEqual(amount,  value.amount)

    # ----------
    # amount__repr__
    # ----------

    def test_amount_repr_1(self) :
        cocktail = Cocktail("Moscow Mule", "Cup", "Moscow Mule Recipe")
        ingredient = Ingredient("Rum")
        amount = Amount(cocktail, ingredient, "2 oz.")
        # amountName = amount.__repr__()
        print(cocktail)
        print(ingredient)
        print(amount.c_data)
        amountName = amount.__repr__()
        self.assertEqual(
            "<Amount [<Cocktail 'Moscow Mule'>-|---|-<Ingredient 'Rum'>]>",
            amountName
        )

    def test_amount_repr_2 (self) :
        cocktail = Cocktail("Vodka Sprite", "glass", "Vodka Sprite Recipe")
        ingredient = Ingredient("Lime")
        amount = Amount(cocktail, ingredient, "1")
        amountName = amount.__repr__()
        self.assertEqual(
            "<Amount [<Cocktail 'Vodka Sprite'>-|---|-<Ingredient 'Lime'>]>",
            amountName
        )

    def test_amount_repr_3 (self) :
        cocktail = Cocktail("Jack and Coke", "cup", "Jack and Coke Recipe")
        ingredient = Ingredient("Coke")
        amount = Amount(cocktail, ingredient, "3 oz.")
        amountName = amount.__repr__()
        self.assertEqual(
            "<Amount [<Cocktail 'Jack and Coke'>-|---|-<Ingredient 'Coke'>]>",
            amountName
        )

# ----
# main
# ----

if __name__ == "__main__" :
    main()
