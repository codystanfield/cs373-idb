import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, \
                           sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
            username='idb_user',
            password='idb_pw',
            hostname='0.0.0.0',
            database='idb')

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
db_session.configure(bind=engine)
Base = declarative_base()
Base.query = db_session.query_property()

# application configureation
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
db = SQLAlchemy(app)
