# GrayQuest Assignment

## Installation
`install.sh` will install all dependencies required to run this application which includes python 3, pip, sqlite database and other required packages which is defined in `requirements.txt.` Additionally, it will ask you for the permission to install the packages.

**Note:** Before executing the `install.sh` script please make sure to go through the file and make necessary changes according to your needs if any.

## Requirements
- Ubuntu 20.04
- Python 3.8
- Pipenv
- Sqlite3 Database

## Run application
In order to run the flask development server execute following commands which will starts the server on http://127.0.0.1:5000

- This command will activate the virtual environment
```
$ pipenv shell
```
- This command will start the flask development server
```
$ python app.py
```

## Database Schema Creation
`database.db` file contains predefined SQLite database schema and users credentials data, however if you want to create your own database schema then delete this file and call the http://127.0.0.1:5000/create-db` api which will create the sqlite database schema file.

## Project Structure Overview
The application consists of 5 directories 7 files along with README.md and .gitignore
- src -> This module contains all the application and sqlalchemy database initialization objects 
- models -> Database connection interface module where SQLAlchemy connection object is created and Users class which 
  represents tables in the database 
- routes -> APIs are defined in this module for this application all the APIs. `auth.py` represents authentication 
  routes and `dashboard.py` represents memes, cookie consent related routes
- static: -> This folder contains CSS and JS files
- templates -> HTML templates are stored here which are used in views of the application
- config.py -> All the application configuration variables are placed in this file
- app.py -> Entry point of the application
- decorators.py -> All decorator functions are placed in this file 
- requirement.txt -> Python packages and dependencies file
