from pydantic import BaseModel

class Users(BaseModel):
    """User Model to store Information

    Args:
        BaseModel : Base Class for all Models
    """
    name: str
    email: str
    city: str
