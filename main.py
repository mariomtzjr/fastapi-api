import email
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from app.schemas import UserRequestModel, UserResponseModel
from app.database import DBConnection
from app.models import User


app = FastAPI(
    title="FastAPI Example",
    description="This is a FastAPI example",
    version="1.0.0",
)
db = DBConnection()

@app.on_event("startup")
def startup():
    """This function validates the database connection,
    if the connection is closed, it will open it.
    """
    print(db)
    if db.is_closed():
        print("Opening database connection")
        db.connect()
        print("Creating tables")
        db.create_tables([User])

@app.on_event("shutdown")
def shutdown():
    """This function validates the database connection,
    if the connection is open, it will close it.
    """
    if not db.is_closed():
        print("Closing database connection")
        db.close()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/users/")
async def read_users():
    users = User.select()
    return [{"username": user.username, "email": user.email} for user in users]

@app.get("/users/{user_id}/")
async def get_user(user_id: int) -> User:
    user = User.select().where(User.id == user_id).first()
    
    if user is not None:
        return UserResponseModel(id=user.id, username=user.username, email=user.email)
    else:
        return HTTPException(status_code=404, detail="User not found")   

@app.post("/users/create/")
async def create_user(user_request: UserRequestModel):
    user_created = User.create(
        username=user_request.username,
        email=user_request.email,
    )
    return {"User created successfully": f"{user_created}"}

@app.put("/users/{user_id}/")
async def update_user(user_id: int, user_request: UserRequestModel):
    user_to_update = User.update(username=user_request.username, email=user_request.email).where(User.id == user_id).execute()
    return {"User updated successfully": f"{UserResponseModel(id=user_id, username=user_request.username, email=user_request.email)}"}
    

@app.delete("/users/{user_id}/")
async def delete_user(user_id: int):
    user = User.select().where(User.id == user_id).first()
    
    if user is not None:
        user.delete_instance()
        return {"User deleted successfully": f"{user}"}
    else:
        return HTTPException(status_code=404, detail="User not found")  