from app.api.dtos.user_dto import UserDto
from uuid import uuid4


class AnUserDto:
    def build(self):
        return UserDto(
            username=f"{uuid4()}",
            password=f"{uuid4()}",
            email=f"{uuid4()}"
        )
