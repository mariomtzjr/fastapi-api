from pydantic import BaseModel


class UserRequestModel(BaseModel):
    """ UserRequestModel
    Determines the structure of the user request model,
    the data type that is passed to the endpoint.
    """

    username: str
    email: str


class UserResponseModel(UserRequestModel):
    id: str