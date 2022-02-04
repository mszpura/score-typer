from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.config import get_session
from app.adapters.repositories.repository import Repository
from app.core.entities.bet import Bet
from app.core.entities.game import Game
from app.core.entities.tournament import Tournament
from app.core.entities.user import User
from app.core.proxies import AbstractRepository


async def compose_users_repository(session: AsyncSession = Depends(get_session)):
    yield Repository("users", User, session)


async def compose_tournaments_repository(session: AsyncSession = Depends(get_session)) -> AbstractRepository:
    yield Repository("tournaments", Tournament, session)


async def compose_games_repository(session: AsyncSession = Depends(get_session)):
    yield Repository("games", Game, session)


async def compose_bets_repository(session: AsyncSession = Depends(get_session)):
    yield Repository("bets", Bet, session)
