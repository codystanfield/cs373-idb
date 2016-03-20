# sample from docs:
# http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
from sqlalchemy import Column, String, Integer
from database import Base


class Cocktail(Base):
    __tablename__ = 'cocktails'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), primary_key=True)
    glass = Column(String(50))
    ingredients = db.relationship('Ingredient', backref='cocktail',
                                  lazy='dynamic')
    recipe = Column(String(1024))
    image = Column(String(128))

    def __init__(self, name, glass, recipe, image=None):
        self.name = name
        self.glass = glass
        self.recipe = recipe
        self.image = image

    def __repr__(self):
        return '<Cocktail %r>' % (self.name)


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id_ = Column(Integer, primary_key=True)
    name = Column(String(50))
    amount = Column(String(50))
    image = Column(String(128))

    def __init__(self, name, amount=None, image=None):
        this.name = name
        this.amount = amount
        this.image = image

    def __repr__(self):
        return '<Ingredient %r>' % (self.name)
