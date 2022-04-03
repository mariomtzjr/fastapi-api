from peewee import *

from .database import DBConnection

db = DBConnection()


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(max_length=50)
    email = CharField(max_length=50)

    def __str__(self):
        return f"{self.username}"


    class Meta:
        table_name = 'users'