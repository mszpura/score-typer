from app.core.entities.bet import Bet
from app.core.entities.game import Game


class BetScoreCalculator:
    def __init__(self,
                 points_per_win: int,
                 points_per_exact_score: int,
                 points_per_typed_scoring_player: int):
        self.points_per_win = points_per_win
        self.points_per_exact_score = points_per_exact_score
        self.points_per_typed_scoring_player = points_per_typed_scoring_player

    def calculate_points_for_bet(self, game: Game, bet: Bet) -> int:
        points_earned = 0

        if game.home.score > game.away.score and bet.home_bet.is_winner:
            points_earned += self.points_per_win
        elif game.away.score > game.home.score and bet.away_bet.is_winner:
            points_earned += self.points_per_win
        elif game.home.score == game.away.score and not bet.home_bet.is_winner and not bet.away_bet.is_winner:
            points_earned += self.points_per_win

        if game.home.score == bet.home_bet.score and game.away.score == bet.away_bet.score:
            points_earned += self.points_per_exact_score

        if bet.home_bet.scored_player and bet.home_bet.scored_player in game.home.scored_players:
            points_earned += self.points_per_typed_scoring_player

        if bet.away_bet.scored_player and bet.away_bet.scored_player in game.away.scored_players:
            points_earned += self.points_per_typed_scoring_player

        return points_earned
