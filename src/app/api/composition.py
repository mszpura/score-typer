from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.config import get_session
from app.adapters.repositories.users_repo import UsersRepository


async def compose_user_repository(session: AsyncSession = Depends(get_session)):
    yield UsersRepository(session)
