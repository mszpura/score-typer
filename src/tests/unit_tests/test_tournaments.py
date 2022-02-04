from app.adapters.repositories.repository import Repository
from tests.arrangers.a_tournament_dto import ATournamentDto


def test_create_tournament(test_app, monkeypatch):
    test_tournament = ATournamentDto().build()

    async def mock_post(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "create", mock_post)

    response = test_app.post("/tournaments", data=test_tournament.json())

    assert response.status_code == 201
    result = response.json()
    assert result["id"]
