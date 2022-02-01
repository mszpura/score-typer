from uuid import uuid4

from app.core.entities.abstract_entity import AbstractEntity


class User(AbstractEntity):
    username: str
    password: str
    email: str

    @classmethod
    def create(cls, **kwargs) -> "User":
        user_id = uuid4()
        return cls(id=str(user_id), **kwargs)

    def update(self, username: str, password: str, email: str) -> None:
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
