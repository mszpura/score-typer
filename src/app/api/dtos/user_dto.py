from uuid import UUID
from pydantic import BaseModel, Field

from app.core.entities.user import User


class UserDto(BaseModel):
    username: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=5, max_length=100)
    email: str = Field(..., min_length=5, max_length=200)

    def to_domain(self, user_id: UUID) -> User:
        return User(str(user_id), self.username, self.password, self.email)
