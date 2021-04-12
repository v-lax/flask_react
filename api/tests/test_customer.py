import pytest
import json
from flaskr.db import get_db

#test function for when our /results route get hit. 
def test_results(client):
  response = client.get('/results')
  data = json.loads(response.data)
  assert len(data['results']) == 11
  assert response.status_code==200
  assert response.headers['Content-Type'] == "application/json"

#test function for when our /add route get hit. 
def test_add(client):
  assert client.get('/add').status_code==405

  response = client.post('/add',data = json.dumps({
    "firstName":'Anthony',
    "lastName":"Davis",
    "email":'adq@test.com',
    "phone":"23425",
    "address":'Fireway street',
    "city":'San Francisco',
    "state":"CA",
    "zip":"234123"
  })).data

  assert b"posted successfully" in response


#the following function are for each different search query scenario. I kept going in 
#circles trying to figure out how to handle all these different scenarios but wasn't able 
#to figure it out so, created a separate function for each scenario. After doing some research
#I may use a parameterized test in pytest (or a test that allows me to run a test against multiple sets of arguments)
def test_state_search(client):
  response = client.get('/search?state=MA').data 
  data = json.loads((response))
  assert len(data['results']) == 2

def test_city_search(client):
  response = client.get("/search?city=Brooklyn")
  data = json.loads(response.data)
  assert len(data['results']) == 2
  assert response.status_code==200

def test_citystate_search(client):
  response=client.get("/search?state=NY&city=Brooklyn")
  data = json.loads(response.data)
  assert len(data['results']) == 2

def test_firstname_search(client):
  response = client.get('/search?firstName=Leb')
  data = json.loads(response.data)
  assert len(data['results']) ==1

def test_lastname_search(client):
  response = client.get('/search?lastName=Ran')
  data = json.loads(response.data)
  assert len(data['results']) ==2

def test_firstlast_search(client):
  response = client.get('/search?firstName=Leb&lastName=jam')
  data = json.loads(response.data)
  assert len(data['results']) == 1

  