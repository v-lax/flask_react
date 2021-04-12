# Customer Data Base for Company XYZ

## Table of Contents 
* [Description](#description)
* [Technologies](#tech)
* [Improvements](#improvements)
* [Resources](#resources)

# Description

The following application is a simple backend application meant to handle GET and POST requests from a front end. It is meant to provide a company with information on all their customers or a specific customer/s based on a search query. The data that is is available for each customer includes, first name, last name, email, phone, address,state,city, and zip. 

The user can filter through the customers in the datbase by City, State, City and State, first name, last name, or First and Last name. The code also includes unit tests that test the endpoints provided for each of the routes. As well! 

Overall this was a really fun project. In my experience I have only used Express, Node, MySQL/Mongo DB to write my backend code. I never used python to write this code before but using the flask framework was intuitive and the resources were abundant. My testing experience (only running test on super simple functions that introduce the topic of testing using mocha js.). I also went a little against protocol and started to build out a little bit of the front
end using react as well. It just allows you add a customer throug form. Nothing to robust as I also needed to write
the tests for this front end code but never got to it. But it was an awesome learning experience in understanding how to test api endpoints as well! Lot of improvements to be made going forward.

# Technologies

The following is a list of all the different technologies used on this project. 

* Python Flask
* pytest for testing
* React for the frontend

Here are some of the reasons I used these technologies. Lets start with flask. Why did I decide to use flask rather than another python framework like Django. Well the main reason was because flask is used at andGo, and I wanted to 
learn up on a new piece of technology that I potentially could use. I choose pytest for one main reason! The tutorial 
that i used to learn flask used pytest for its unit testing! But I do know that there are some benefits to using pytest. Pytest can allow us to run multiple tests in parallel. It can detect all of our test files and test functions automatically and provides us with simple syntax. I installed react because i wanted to try my hand and build out a little bit of front end. I built out a simple add customer button that posted form data from local host 3000 to our server which was running on local host 5000. 

If you want to take a look at the front end code you can do so -> https://github.com/v-lax/flask_react

# Improvements 

There are a lot of different things that I would come back and improve next time around for future iterations. This was my first time using python and flask for my back end as well as my first time writing tests for my API endpoints. Below are a list of tasks/features that I would come back and implement on another go around with more experience under my belt. 

* Improve the search query functionality. The api can currently handle 6 different types of searches but for more complicated versions, I would want to think long and hard about what the front end would like and what could be entered in by the user to then build out more robust search query function. 

* In my tests, I wrote 6 different test functions (one for each search query). Why did I do this? I didn't know how to handle all of these search parameters in one test function. But I came across pytest's capability to do a parameterized test, and would use that to refactor those 6 test functions mentioned above.

* My test are pretty simple. I wouuld come back and potentially add more assertions that deal with edge cases for my endpoints. Kind of going off this, I would also love to learn how I could deploy these tests into a build server of some kind so that when we push code, this code automatically gets tested and the developer gets sent an email with said results of that test. This is mostly because my ci/cd experience is minimal but I would love to learn more about that.

# Sources 

There is no way I could have done this on my own. I never used python flask before so I spent a long time reading through their documentation and going through their tutorial (much of which my code is based on) and also spent time watching lots of youtube videos on testing api endpoints. Below are the resources that I used to complete this assignment.

* [Flask docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
* [React+Flask](https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project)
* [FlaskVideoTutorial](https://www.youtube.com/watch?v=hbDRTZarMUw&list=PLCC34OHNcOtqJBOLjXTd5xC0e-VD3siPn&index=8)
* [UnitTesting](https://flask.palletsprojects.com/en/1.1.x/tutorial/tests/)