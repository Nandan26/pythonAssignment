
def get_json(user) -> dict:
    """Coverts into dictionary

    Args:
        user (User): instance of user class

    Returns:
        dict: dictionary having data of User
    """
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "city": user["city"]
    }

def users_json(users) -> list:
    """gets Multiple users as input and returns list of dictionary

    Args:
        users (User): list of User

    Returns:
        list: list of dictionary
    """
    return [get_json(user) for user in users]
