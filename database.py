import pickle
from config import logger, \
                   engine,\
                   db_session, \
                   Base, \
                   app, \
                   manager
from models import Cocktail, \
                   Ingredient, \
                   Amount
from DBScraper import Cocktail_


@manager.command
def init_db():
  # logger.debug("init_db")
  # app.config['SQLALCHEMY_ECHO'] = True
  Base.metadata.create_all(engine)


@manager.command
def load_pickled_data():
  with open('cocktails.pkl', 'rb') as f:
    pickled_cocktails = pickle.load(f)

  for c in pickled_cocktails:
    # instantiate and add cocktail
    cocktail = Cocktail(name=c.name, glass=c.glass, recipe=c.recipe, image=c.image)
    db_session.add(cocktail)

    # add each ingredient that is not already in db
    for i in c.ingredients:
        ingredient = Ingredient.query.filter(Ingredient.name==i[0]).one_or_none()
        if ingredient is None:
            image_name = i[0].replace(' ', '+').replace('/', '\\')
            image_path = '{0}/{1}'.format('ingredients', image_name)

            ingredient = Ingredient(i[0], image_path)

        db_session.add(ingredient)

        # add the amount for each ingredient
        amount = Amount(cocktail, ingredient, i[1])
        db_session.add(amount)
    # commit unpickled cocktail goodness
    db_session.commit()


@manager.command
def drop_db():
    # db_session.close()
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    manager.run()
