import os

from peewee import *


class DBConnection:

    _instance = None

    def __new__(cls, *args, **kwargs):
        db = MySQLDatabase(
            'fastapi_database',
            user='root', password=os.environ.get("MYSQL_ROOT_PASSWORD"),
            host='localhost', port=3306
        )

        if cls._instance is None:
            cls._instance = super().__new__(DBConnection)
            cls._instance = db
            return cls._instance
        return db

    def __init__(self) -> None:
        self.db = self._instance