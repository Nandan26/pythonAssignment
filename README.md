# pythonAssignment

# FastAPI CRUD operation on user database stored on MongoDB atlas

## Required libraries/frameworks

1. fastAPI
2. uvicorn
3. pymongo

## main.py

contains routes for API and this main file is executed first when server runs

## database.py

It is responsible for connecting with database hosted on mongodb atlas and create collection in it if not exist 

## data_model.py

To define User Model and attributes of it

## user_schemas.py

Converting object of User model into json like format so it can be returned as response 
