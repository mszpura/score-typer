from uuid import uuid4, UUID

from app.core.entities.user import User


class AnUser:
    def __init__(self):
        self.user_id = f"{uuid4()}"

    def with_id(self, _id: UUID):
        self.user_id = str(_id)
        return self

    def build(self):
        return User(id=self.user_id, username=f"{uuid4()}", password=f"{uuid4()}", email=f"{uuid4()}")


class SomeUsers:
    def build(self, amount):
        users = []
        for i in range(amount):
            users.append(AnUser().build())
        return users

