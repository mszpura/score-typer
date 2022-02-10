from typing import List
from uuid import uuid4

from datetime import datetime

import pytest

from app.core.bet_score_calculator import BetScoreCalculator
from app.core.entities.bet import Bet
from app.core.entities.game import Game


@pytest.mark.parametrize(
    "game_home_score, game_away_score, game_home_scored_players, game_away_scored_players, bet_home_score, bet_away_score, bet_is_home_wins, bet_is_away_wins, bet_home_scorer, bet_away_scorer, expected_score",
    [
        [2, 1, [12, 31], [45], 2, 1, True, False, 12, None, 6],
        [2, 4, [12, 31], [45, 1, 17, 3], 2, 4, False, True, 12, None, 6],
        [2, 4, [12, 31], [45, 1, 17, 3], 2, 4, False, True, None, 17, 6],
        [2, 2, [12, 31], [12, 31], 2, 2, False, False, None, 12, 6],
        [2, 3, [12, 13], [11, 1, 7], 2, 3, True, False, None, 11, 5],
        [0, 0, [], [], 0, 0, False, False, None, 17, 4],
        [3, 1, [12, 13, 14], [11], 2, 1, True, False, None, 11, 3],
        [2, 1, [7, 5], [23], 4, 2, True, False, 12, None, 1],
        [0, 0, [], [], 2, 3, True, False, None, 11, 0],
    ]
)
def test_calculates_score_correctly(
        game_home_score: int,
        game_away_score: int,
        game_home_scored_players: List[int],
        game_away_scored_players: List[int],
        bet_home_score: int,
        bet_away_score: int,
        bet_is_home_wins: bool,
        bet_is_away_wins: bool,
        bet_home_scorer: int,
        bet_away_scorer: int,
        expected_score: int):
    # Arrange
    test_game = Game.create(uuid4(), "some_team_1", "some_team_2")
    test_bet = Bet.create(test_game.id, uuid4(), bet_home_score, bet_away_score, bet_is_home_wins, bet_is_away_wins,
                          bet_home_scorer, bet_away_scorer)
    test_game.finish(datetime.now(), game_home_score, game_away_score, game_home_scored_players,
                     game_away_scored_players)

    calculator = BetScoreCalculator(1, 3, 2)

    # Act
    result = calculator.calculate_points_for_bet(test_game, test_bet)

    # Assert
    assert result == expected_score
