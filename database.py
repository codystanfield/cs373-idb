# import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, \
                           sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URI = '{engine}://{username}:{password}@{hostname}/{database}'.format(
            engine='mysql+pymysql',
            username='idb_user',
            password='idb_pw',
            hostname='0.0.0.0',
            database='idb')

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db_():
  Base.metadata.create_all(bind=engine)


def load_pickled_data_():
  pass
  # logger.debug("create_test_data")
  # app.config['SQLALCHEMY_ECHO'] = True
  # guest = Guest(name='Steve')
  # db.session.add(guest)
  # db.session.commit()

# @manager.command
# def drop_db():
#     logger.debug("drop_db")
#     app.config['SQLALCHEMY_ECHO'] = True
#     db.drop_all()
