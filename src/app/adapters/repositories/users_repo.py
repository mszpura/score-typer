import uuid
from typing import List

from app.core.entities.user import User
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.proxies import AbstractRepository


class UsersRepository(AbstractRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User):
        await self.session.execute(
            f"INSERT INTO users (id, json) VALUES (:id, :json)",
            {"id": uuid.UUID(user.id), "json": user.json()})
        await self.session.commit()

    async def get(self, id: uuid.UUID) -> User | None:
        result = await self.session.execute(
            f"SELECT json FROM users WHERE id = :id",
            {"id": str(id)})
        user = result.fetchone()
        if user is not None:
            return self.map_user(user)
        return None

    async def get_all(self) -> List[User]:
        result = await self.session.execute("SELECT * FROM users")
        return list(map(self.map_user, result.fetchall()))

    async def update(self, user: User):
        await self.session.execute(
            f"UPDATE users SET json = :json WHERE id = :id",
            {"json": user.json(), "id": uuid.UUID(user.id)})
        await self.session.commit()

    async def delete(self, user_id: uuid.UUID):
        await self.session.execute("DELETE FROM users WHERE id = :id", {"id": user_id})
        await self.session.commit()

    @staticmethod
    def map_user(user):
        return User(**user["json"])
