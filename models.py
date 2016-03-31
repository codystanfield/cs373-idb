# http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
from sqlalchemy import Column, \
                       String, \
                       Integer, \
                       Sequence, \
                       ForeignKey
from config import db, \
                   Base


class Cocktail(Base):
    """Cocktail model.

    Contains cocktail attributes and a one-to-many relationship to Ingredients

    Attributes:
        __tablename__: A string, the database table name.
        id_: An integer representing primary key sequence.
        name: A string. The name of the cocktail.
        glass: A string indicating the recommended glass for consumption.
        ingredients: One-to-many relationship with amounts.
        recipe: A string with directions to make the cocktail.
        image: A string indicating the folder/filename for a static image.
    """
    __tablename__ = 'cocktails'
    id_ = Column(Integer,  Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    glass = Column(String(50))
    ingredients = db.relationship('Amount', backref='c_data', lazy='dynamic')
    recipe = Column(String(1024))
    image = Column(String(128))

    def __init__(self, name, glass, recipe, image=None):
        """Inits Cocktail with name, glass, recipe, and image."""
        self.name = name
        self.glass = glass
        self.recipe = recipe
        self.image = image

    def __repr__(self):
        """Returns a string representation of an Ingredient."""
        return '<Cocktail %r>' % (self.name)


class Ingredient(Base):
    """Ingredient model.

    Contains ingredient attributes.

    Attributes:
        __tablename__: A string, the database table name.
        id_: An integer representing primary key sequence.
        name: A string. The name of the ingredient.
        cocktails: One-to-many relationship to amounts.
        image: A string indicating the folder/filename for a static image.
    """
    __tablename__ = 'ingredients'
    id_ = Column(Integer,  Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    cocktails = db.relationship('Amount', backref='i_data', lazy='dynamic')
    image = Column(String(128))

    def __init__(self, name, image=None):
        """Inits Ingredient with name, amount, and image."""
        self.name = name
        self.image = image

    def __repr__(self):
        """Returns a string representation of an Ingredient."""
        return '<Ingredient %r>' % (self.name)


class Amount(Base):
    """Models the many-to-many relationship between Cocktails and Ingredients.

    Contains foreign keys to cocktails and ingredients to relate rows in the
    two tables. Hold the amount of an ingredient to be used in a cocktail as a
    relationship attribute.

    Attributes:
        __tablename__: A string, the database table name.
        id_: An integer representing primary key sequence.
        amount: A string indicating the amount of this ingredient required for
                this cocktail.
        cocktail_id = Column(Integer, ForeignKey('cocktails.id_'))
        ingredient_id = Column(Integer, ForeignKey('ingredients.id_'))
    """
    __tablename__ = '__amounts__'
    id_ = Column(Integer,  Sequence('amount_seq'), primary_key=True)
    cocktail = Column(Integer, ForeignKey('cocktails.id_'))
    ingredient = Column(Integer, ForeignKey('ingredients.id_'))
    amount = Column(String(50))

    def __init__(self, cocktail, ingredient, amount):
        """Inits Amount by adding this object to the one-to-many relationships
        in cocktails and ingredients and saving amount."""
        cocktail.ingredients.append(self)
        ingredient.cocktails.append(self)
        self.amount = amount

    def __repr__(self):
        """Returns a string representation of an Amount relationship."""
        return '<Amount [%r-|---|-%r]>' % (self.c_data, self.i_data)
