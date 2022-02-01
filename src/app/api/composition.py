from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.config import get_session
from app.adapters.repositories.repository import Repository
from app.core.entities.user import User


async def compose_user_repository(session: AsyncSession = Depends(get_session)):
    # yield UsersRepository(session)
    yield Repository("users", User, session)
