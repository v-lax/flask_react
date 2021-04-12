#the following file will contain all of the necesarry setup functions(otherwise known as fixtures) that
#each of our tests will use. 

#for all of these fixtures, pytest is able to match the correct function name with the
#arguments passed into the test functions.

import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

#our app fixture will call the factory we created and pass in the testing configuration
#variables to configure the application and database for testing instead of using 
#the local development configuration we were using wher running our flask app normally.
@pytest.fixture
def app():
  #create and open a temp file but not the one we created before. The database path is
  #overridden so that it points to this temp folder rather than the instance folder
  #we created before. After we finish thes test the temp folder is closed and removed
  db_fd, db_path = tempfile.mkstemp()
  app = create_app({
    'TESTING':True,
    'DATABASE':db_path,
  })

  with app.app_context():
    init_db()
    get_db().executescript(_data_sql)

  yield app

  os.close(db_fd)
  os.unlink(db_path)

#set up a fixture so that the tests will be able to use a client to make requests
#to the application without having to run the server.
@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
