#the file helps us connect to our database, and run any sql scripts that we mention. The reason
#we are using sqlite is because for an application of this size it was easy to just 
#use the built in support for SQLlite. It doesnt require setting up a separate database server
#and is already built into python. BUT, as the size of our application grows, SQLite may not
#be the best option because of size, concurrent requests and more. 

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


#the following function establishes a connection to our database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

#this function checks to see if a connection was created and if it does it is closed.
#we will use to close our database after each request in our application
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
#function that initializes our database by using the schema.sql file and executes that script.
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

#the close database function and init database function mentioned above have to 
#be registered with our application and this function does just that.
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)