#the following file handles all of the logic for the different routes setup for our 
#application. It contains all of the view function for applications. These are 
#just functions that respond to requests to our application. A group of these view functions
#is what is known as a blueprint. It is a way of organizing a group of related view functions. 
#After we create our blueprint function we then registter this blueprint function with the 
#application factory function that we created. 

import json
from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for, Response
)

from flaskr.db import get_db

bp = Blueprint('customer', __name__)

#this function deals with the /results route. It returns all the 
#records in the database. 
@bp.route('/results',methods=['GET'])
def index():
  if request.method=='GET':
    resultsArray =[]
    response = {}
    db = get_db()
    cur = db.cursor()
    cur.execute(
      "SELECT * FROM customer"
    )
    rows = cur.fetchall()
    for row in rows:
      results = {}
      results['firstName'] = row['firstName']
      results['lastName'] = row['lastName']
      results['email'] = row['email']
      results['phone'] = row['phone']
      results['address'] = row['address']
      results['city'] = row['city']
      results['state'] = row['state']
      results['zip']=row['zip']
      resultsArray.append(results)
    response['results'] = resultsArray
    db.commit()
    return response
  
    

#this function deals with the /add route. It will be called when
#a user adds a customer to our database. Upon successful insertion
#of record into the database, the user will recieve a message saying 
#that the record was successfully added. 
@bp.route('/add',methods=['POST'])
def add():
  if request.method=="POST":
    data = request.get_json(force=True)

    firstname = data["firstName"]
    lastname = data["lastName"]
    email = data["email"]
    phone = data['phone']
    address = data['address']
    city = data['city']
    state = data['state']
    zipCode = data['zip']

    db = get_db()
    db.execute(
      'INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)'
      'VALUES (?,?,?,?,?,?,?,?)',
      (firstname,lastname,email,phone,address,city,state,zipCode)
     )
    db.commit()
    #A few notes here. In our sql schema we set it up so that specific colums must be
    #unique. If the user tries to add a duplicate record, our database will not 
    #allow it. I did not have enough time to handle that error but would send back
    #the necessary response message if we did recieve that error, along with the correct
    #error code. 
    return "posted successfully"

#this function handles our search requests. This one was the big one. It uses the 
#query parameters that come in through the url and using the query parameters 
#we search our database accordingly and return the necessary records that match
#that query. I tried my best to set up this function handle all types of 
#search requests. It is currently set up to handle the following searches. 
#Search by State 
#Search by City 
#Search by State and City
#Search by first name (partial strings)
#Search by last name (partial strings)
#Search by both first and last name (partial strings)
#I think that a more robust search function can be set
#up, if I was able to work with the front end team and understand
#what search functionalities they would want and set up the backend
#accordingly. I also tried my best to answer the bonus question where
#we needed to return all records from California, Florida, and Chicago. 
# I wasnt sure whether or not that meant all records that had a city chicago, or a state of
#california or a state of florida, OR if that meant return records where the state was California and the city was chicago
#I think that by clarifying this with the front end team and understanding the limits 
#of the search functionalities we want to implement, I could clarify the confusion regarding 
#this query and design a better search function.
@bp.route('/search')
def search():
  args = request.args
  resultsArray = []
  response = {}

  if all (k in args for k in ("state","city")):
    state = args['state']
    city = args['city']
    db = get_db()
    cur = db.cursor()
    cur.execute(
      "SELECT * FROM customer WHERE state = ? AND city = ?", [state,city]
    )
    rows = cur.fetchall()
    for row in rows:
      results = {}
      results['firstName'] = row['firstName']
      results['lastName'] = row['lastName']
      results['email'] = row['email']
      results['phone'] = row['phone']
      results['address'] = row['address']
      results['city'] = row['city']
      results['state'] = row['state']
      results['zip']=row['zip']
      resultsArray.append(results)
    
    if(len(resultsArray)==0):
      return Response("{'message':'data not found'}", mimetype='application/json')
  
  elif 'state' in args:
    state = args['state']
    db = get_db()
    cur = db.cursor()
    cur.execute(
      "SELECT * FROM customer WHERE state = ?", [state]
    )
    rows = cur.fetchall()
    for row in rows:
      results = {}
      results['firstName'] = row['firstName']
      results['lastName'] = row['lastName']
      results['email'] = row['email']
      results['phone'] = row['phone']
      results['address'] = row['address']
      results['city'] = row['city']
      results['state'] = row['state']
      results['zip']=row['zip']
      resultsArray.append(results)
    
    if(len(resultsArray)==0):
      return Response({"message":"data not found"}, mimetype='application/json')

  elif "city" in args:
    city = args['city']
    print(city)
    db = get_db()
    cur = db.cursor()
    cur.execute(
      "SELECT * FROM customer WHERE city = ?", [city]
    )
    rows = cur.fetchall()
    for row in rows:
      results = {}
      results['firstName'] = row['firstName']
      results['lastName'] = row['lastName']
      results['email'] = row['email']
      results['phone'] = row['phone']
      results['address'] = row['address']
      results['city'] = row['city']
      results['state'] = row['state']
      results['zip']=row['zip']
      resultsArray.append(results)

    if(len(resultsArray)==0):
      return Response("{'message':'data not found'}", mimetype='application/json')
  
  elif all (k in args for k in ("firstName","lastName")):
    firstName = args['firstName']
    lastName = args['lastName']
    db = get_db()
    cur = db.cursor()
    cur.execute(
      "SELECT * FROM customer WHERE firstName LIKE '%'||?||'%' AND lastName LIKE '%'||?||'%'", [firstName,lastName]
    )
    rows = cur.fetchall()
    for row in rows:
      results = {}
      results['firstName'] = row['firstName']
      results['lastName'] = row['lastName']
      results['email'] = row['email']
      results['phone'] = row['phone']
      results['address'] = row['address']
      results['city'] = row['city']
      results['state'] = row['state']
      results['zip']=row['zip']
      resultsArray.append(results)
    
    if(len(resultsArray)==0):
      return Response("{'message':'data not found'}", mimetype='application/json')

  elif "firstName" in args:
    firstName = args['firstName']

    db = get_db()
    cur = db.cursor()
    cur.execute(
      "SELECT * FROM customer WHERE firstName LIKE '%'||?||'%' ", [firstName]
    )
    rows = cur.fetchall()
    for row in rows:
      results = {}
      results['firstName'] = row['firstName']
      results['lastName'] = row['lastName']
      results['email'] = row['email']
      results['phone'] = row['phone']
      results['address'] = row['address']
      results['city'] = row['city']
      results['state'] = row['state']
      results['zip']=row['zip']
      resultsArray.append(results)

    if(len(resultsArray)==0):
      return Response("{'message':'data not found'}", mimetype='application/json')
  
  elif "lastName" in args:
    lastName = args['lastName']

    db = get_db()
    cur = db.cursor()
    cur.execute(
      "SELECT * FROM customer WHERE lastName LIKE '%'||?||'%' ", [lastName]
    )
    rows = cur.fetchall()
    for row in rows:
      results = {}
      results['firstName'] = row['firstName']
      results['lastName'] = row['lastName']
      results['email'] = row['email']
      results['phone'] = row['phone']
      results['address'] = row['address']
      results['city'] = row['city']
      results['state'] = row['state']
      results['zip']=row['zip']
      resultsArray.append(results)
    
    if(len(resultsArray)==0):
      return Response("{'message':'data not found'}", mimetype='application/json')

  else:
    print('wrong query')
    return Response("{'message':'bad query'}", status=400, mimetype='application/json')

  response['results'] = resultsArray
  return response 