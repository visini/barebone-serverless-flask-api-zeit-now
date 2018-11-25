#database.py
import importlib.machinery
from distutils.sysconfig import get_python_lib
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

# if local environment, use psycopg2 installed in python library (site-packages), otherwise use from binary (psycopg2 subdirectory in this folder)
try:
    psycopg2 = importlib.machinery.SourceFileLoader('psycopg2', get_python_lib()+'/psycopg2/__init__.py').load_module()
except:
    import psycopg2

username = "xxx"
databasename = "xxx"
host = "xxx.eu-west-1.rds.amazonaws.com"
password = "xxx"

engine = create_engine('postgres://{}:{}@{}/{}'.format(username, password, host, databasename), convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    metadata.create_all(bind=engine)
