import json
from uuid import uuid4

import pytest

from app.adapters.repositories.repository import Repository
from app.core.entities.game import Game
from app.infrastructure.uuid_encoder import UUIDEncoder
from tests.arrangers.a_game_dto import AGameDto


def test_create_game(test_app, monkeypatch):
    test_game = AGameDto().build()

    async def mock_post(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "create", mock_post)

    response = test_app.post("/games", data=test_game.json())
    assert response.status_code == 201


@pytest.mark.parametrize(
    "payload, status_code",
    [
        [{"home_team_name": f"{uuid4()}"}, 422],
        [{"away_team_name": f"{uuid4()}"}, 422],
        [{"tournament_id": uuid4()}, 422],
        [{"home_team_name": f"{uuid4()}", "tournament_id": uuid4()}, 422],
        [{"home_team_name": f"{uuid4()}", "away_team_name": f"{uuid4()}"}, 422],
        [{"tournament_id": uuid4(), "home_team_name": f"{uuid4()}", "away_team_name": f"{uuid4()}"}, 201]
    ]
)
def test_create_game_properly_validate_input_data(test_app, monkeypatch, payload, status_code):
    async def mock_post(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "create", mock_post)

    response = test_app.post("/games", data=json.dumps(payload, cls=UUIDEncoder))
    assert response.status_code == status_code


def test_read_game(test_app, monkeypatch):
    test_data = Game.create(**AGameDto().build().dict())

    async def mock_get(_self, _game_id):
        return test_data
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.get(f"/games/{uuid4()}")
    assert response.status_code == 200
    assert response.json() == json.loads(test_data.json())
