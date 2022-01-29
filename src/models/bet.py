from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from .game import Game
from .user import User


@dataclass
class TeamBet:
    score: int
    is_winner: bool
    scored_player: Optional[int]


@dataclass()
class Bet:
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
               away_scorer: Optional[int]):

        if home_scorer is None and away_scorer is None:
            raise AttributeError(f"No scorer has been selected")

        home_bet = TeamBet(home_score, is_home_wins, home_scorer)
        away_bet = TeamBet(away_score, not is_home_wins, away_scorer)
        return Bet(_id, game, user, home_bet, away_bet)
