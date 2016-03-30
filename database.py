# import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# DBUSER = 'idb_user'
# DBPASSWD = 'idb_pw'
# DBHOSTNAME = 'localhost'
# DBPORT = '5432'
# DBNAME = 'idb'

# postgresql+psycopg2://idb_user:idb_pw@localhost:5432/idb
# SQLALCHEMY_DATABASE_URI = ('postgresql+psycopg2://' +
#                            DBUSER + ':' +
#                            DBPASSWD +  '@' +
#                            DBHOSTNAME + ':' +
#                            DBPORT + '/' +
#                            DBNAME)
# SQLALCHEMY_DATABASE_URI = \
#     '{engine}://{username}:{password}@{hostname}/{database}'.format(
#         engine='mysql+pymysql',
#         username=os.getenv('MYSQL_USER'),
#         password=os.getenv('MYSQL_PASSWORD'),
#         hostname=os.getenv('MYSQL_HOST'),
#         database=os.getenv('MYSQL_DATABASE'))
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
  # import all modules here that might define models so that
  # they will be registered properly on the metadata.  Otherwise
  # you will have to import them first before calling init_db()
  import models
  Base.metadata.create_all(bind=engine)

# @manager.command
# def create_db():
#     logger.debug("create_db")
#     app.config['SQLALCHEMY_ECHO'] = True
#     db.create_all()
#
# @manager.command
# def create_dummy_data():
#     logger.debug("create_test_data")
#     app.config['SQLALCHEMY_ECHO'] = True
#     guest = Guest(name='Steve')
#     db.session.add(guest)
#     db.session.commit()
#
# @manager.command
# def drop_db():
#     logger.debug("drop_db")
#     app.config['SQLALCHEMY_ECHO'] = True
#     db.drop_all()
