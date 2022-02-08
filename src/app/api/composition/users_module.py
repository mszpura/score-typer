from typing import Text
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.config import get_session
from app.adapters.repositories.repository import Repository
from app.api.dtos.user_dto import UserDto
from app.core.entities.user import User
from app.core.proxies import AbstractRepository
from app.api.routes.crud_route_factory import create_crud_router_for


async def compose_users_repository(session: AsyncSession = Depends(get_session)) -> AbstractRepository:
    yield Repository("users", User, session)


def add_users_routing(app: FastAPI, prefix: Text):
    routes = create_crud_router_for(User, compose_users_repository, UserDto)
    app.include_router(routes, prefix=f"/{prefix}", tags=[prefix])
