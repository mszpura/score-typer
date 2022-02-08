from typing import Text

from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.config import get_session
from app.adapters.repositories.repository import Repository
from app.api.dtos.tournament_dto import TournamentDto
from app.api.routes.crud_route_factory import create_crud_router_for
from app.core.entities.tournament import Tournament
from app.core.proxies import AbstractRepository


async def compose_tournaments_repository(session: AsyncSession = Depends(get_session)) -> AbstractRepository:
    yield Repository("tournaments", Tournament, session)


def add_tournaments_routing(app: FastAPI, prefix: Text):
    routes = create_crud_router_for(Tournament, compose_tournaments_repository, TournamentDto)
    app.include_router(routes, prefix=f"/{prefix}", tags=[prefix])
