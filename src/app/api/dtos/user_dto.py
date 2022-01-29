from pydantic import BaseModel, Field


class UserDto(BaseModel):
    username: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=5, max_length=100)
    email: str = Field(..., min_length=5, max_length=200)


class UserDb(UserDto):
    id: int
