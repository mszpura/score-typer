from app.adapters.repositories.repository import Repository
from tests.arrangers.a_game_dto import AGameDto


def test_create_game(test_app, monkeypatch):
    test_game = AGameDto().build()

    async def mock_post(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "create", mock_post)

    response = test_app.post("/games", data=test_game.json())
    assert response.status_code == 201

