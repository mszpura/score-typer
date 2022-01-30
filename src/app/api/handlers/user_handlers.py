from app.adapters.postgres_repository.users_repo import UsersRepository
from app.api.dtos.user_dto import UserDto
from app.adapters.db.config import async_session
from uuid import uuid4, UUID


async def create(payload: UserDto):
    async with async_session() as session:
        async with session.begin():
            user_id = uuid4()
            user = payload.to_domain(user_id)
            await UsersRepository(session).create(user)
            return user


async def get_by(user_id: UUID):
    async with async_session() as session:
        async with session.begin():
            return await UsersRepository(session).get(user_id)