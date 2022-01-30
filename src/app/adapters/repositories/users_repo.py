import uuid
from typing import List

from app.core.entities.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime


async def create(user: User, session: AsyncSession):
    await session.execute(
        f"INSERT INTO users (id, json, created_date) VALUES (:id, :json, :created_date)",
        {"id": uuid.UUID(user.id), "json": user.json(), "created_date": datetime.now()})


async def get(id: uuid.UUID, session: AsyncSession) -> User | None:
    result = await session.execute(
        f"SELECT json FROM users WHERE id = :id",
        {"id": str(id)})
    user = result.fetchone()
    if user is not None:
        return map_user(user)
    return None


async def get_all(session: AsyncSession) -> List[User]:
    result = await session.execute("SELECT * FROM users")
    return list(map(map_user, result.fetchall()))


async def update(user: User, session: AsyncSession):
    await session.execute(
        f"UPDATE users SET json = :json WHERE id = :id",
        {"json": user.json(), "id": uuid.UUID(user.id)})


async def delete(user_id: uuid.UUID, session: AsyncSession):
    await session.execute("DELETE FROM users WHERE id = :id", {"id": user_id})


def map_user(user):
    return User(**user["json"])
