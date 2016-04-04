import pickle
from config import logger, \
                   engine,\
                   Base, \
                   app, \
                   manager
from models import Cocktail, \
                   Ingredient, \
                   Amount


@manager.command
def init_db():
  logger.debug("init_db")
  app.config['SQLALCHEMY_ECHO'] = True
  Base.metadata.create_all(engine)
  # from config import db
  # db.create_all()


@manager.command
def load_pickled_data():
  with open('cocktails.pkl', 'wb') as f:
    pickled_cocktails = pickle.load(f)

  for c in pickled_cocktails:
    # instantiate model
    cocktail = Cocktail(c.name, c.glass, c.recipe, c.image)

    # for i in c.ingredients:
    #   if ingredient.name is unique
    #   if Base.query.returns_rows(__ingredients__, 'name'=i[0]):
    #     add it to the ingredients table
    #     db_session.add(ingredient)
    #   instantiate ingredient from table
    #   instantiate amount
    #   amount = Amount(cocktail, ingredient, i[1])
    #   db_session.add(amount)


    # ...or save/commit here?


@manager.command
def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    manager.run()
