from typing import Text

from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.config import get_session
from app.adapters.repositories.repository import Repository
from app.api.dtos.game_dto import GameDto
from app.api.routes.crud_route_factory import create_crud_router_for
from app.core.entities.game import Game
from app.core.proxies import AbstractRepository


async def compose_games_repository(session: AsyncSession = Depends(get_session)) -> AbstractRepository:
    yield Repository("games", Game, session)


def add_games_routing(app: FastAPI, prefix: Text):
    routes = create_crud_router_for(Game, compose_games_repository, GameDto)
    app.include_router(routes, prefix=f"/{prefix}", tags=[prefix])
