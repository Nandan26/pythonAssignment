from bson import ObjectId
from fastapi import FastAPI
from database import user_info
from user_schema import users_json
from data_Model import Users

#initialize the app
app = FastAPI()

@app.get("/")
async def main_page():
    """home page

    Returns:
        message
    """
    return {"message": "Welcome to the User Information API"}

@app.get("/users")
async def get_users():
    """return all the users

    Returns:
        dict: all the users from database
    """

    todos = users_json(user_info.find())

    return todos

@app.get("/{id}")
async def get_user(id: str):
    """list user who has given id

    Args:
        id (str): user id you want to fetch

    Returns:
        dict: user information
    """
    return users_json(user_info.find_one({"_id": ObjectId(id)}))


@app.post("/")
async def create_user(user: Users):
    """add new user

    Args:
        user (Users): instance of Users class

    Returns:
        dict: added user
    """
    _id = user_info.insert_one(dict(user))
    return users_json(user_info.find({"_id": _id.inserted_id}))

@app.put("/{id}")
async def update_user(id: str, user: Users):
    """update the existing user

    Args:
        id (str): id of the user you want to update
        user (Users): updated values

    Returns:
        dict: updated values of user 
    """
    user_info.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })

    return users_json(user_info.find({"_id": ObjectId(id)}))

@app.delete("/{id}")
async def delete_user(id: str):
    """delete the user who has given id

    Args:
        id (str): id of the user you want to delete

    Returns:
        dict : deleted successfully
    """
    user_info.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "Deleted Successfully"}