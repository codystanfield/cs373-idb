# logging
import logging
# database
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, \
                           sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# app: idb.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager


# logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("-----app logging initiated-----")


# database configuration
SQLALCHEMY_DATABASE_URI = '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))
logger.debug("The log statement below is for development purposes only. Remove and clean logs before deployment.")
logger.debug("SQLALCHEMY_DATABASE_URI: %s", SQLALCHEMY_DATABASE_URI)

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
db_session.configure()
Base = declarative_base()
Base.query = db_session.query_property()

# application configuration
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
db = SQLAlchemy(app)
