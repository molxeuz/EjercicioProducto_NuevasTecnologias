# user.py
from abc import ABC, abstractmethod
from database.connection import DataBase

class User(ABC):
    def __init__(self, username):
        self.username = username
    @abstractmethod
    def perform_action(self, db):
        pass
    def get_username(self):
        return self.username
    @classmethod
    def authenticate(cls, username, password):
        db = DataBase()
        user_type = db.authenticate(username, password)
        return user_type