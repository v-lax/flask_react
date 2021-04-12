#in order to create a flask application we need to create an instance of flask. Most
#simple way to create one may be to add it to the top of your main server file but may
#potentially cause issues down the line if your project grows. Instead we will create that 
#flask application inside of a function known as the application factory. Any configuration
#or setup that needs to happen can happen inside of this function. 

import os
from flask import Flask,request


def create_app(test_config=None):
    # create the isntance of flask and stores it in a variable called app.
    app = Flask(__name__, instance_relative_config=True)
    #here we setup the default configuration of our application
    app.config.from_mapping(
        #the secret key is used by flask to keep the data in our database safe. 
        #when we deploy to a production environement we can overide this value with
        #a random value and store that value in config.py file. Database is the path
        #to the SQLite database we create
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #code that we import in from out db.py file. This will initialize our database.
    from . import db
    db.init_app(app)

    #import in our customer.py file which contains all of the logic for handling 
    #all the different routes. 
    from . import customer
    app.register_blueprint(customer.bp)

    return app