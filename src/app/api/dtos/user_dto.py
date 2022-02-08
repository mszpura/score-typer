from pydantic import Field

from app.core.entities.abstract_entity import AbstractDto


class UserDto(AbstractDto):
    username: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=5, max_length=100)
    email: str = Field(..., min_length=5, max_length=200)
