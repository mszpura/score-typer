from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from .abstract_entity import AbstractEntity
from .game import Game
from .user import User


class TeamBet(BaseModel):
    score: int
    is_winner: bool
    scored_player: Optional[int]


class Bet(AbstractEntity):
    id: UUID
    game: Game
    owner: User
    home_bet: TeamBet
    away_bet: TeamBet

    @classmethod
    def create(cls,
               _id: UUID,
               game: Game,
               user: User,
               home_score: int,
               away_score: int,
               is_home_wins: bool,
               home_scorer: Optional[int],
               away_scorer: Optional[int]) -> "Bet":

        if home_scorer is None and away_scorer is None:
            raise AttributeError(f"No scorer has been selected")  # TODO: domain error

        home_bet = TeamBet(score=home_score, is_winner=is_home_wins, scored_player=home_scorer)
        away_bet = TeamBet(score=away_score, is_winner=not is_home_wins, scored_player=away_scorer)
        return Bet(id=_id, game=game, user=user, home_bet=home_bet, away_bet=away_bet)
