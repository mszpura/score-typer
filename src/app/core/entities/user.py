from typing import Text
from uuid import uuid4

from .abstract_entity import AbstractEntity


class User(AbstractEntity):
    username: Text
    password: Text
    email: Text

    @classmethod
    def create(cls, **kwargs) -> "User":
        return cls(id=str(uuid4()), **kwargs)

    def update(self, username: str, password: str, email: str) -> None:
        self.username = username
        self.password = password
        self.email = email
