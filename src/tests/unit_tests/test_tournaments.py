import json
from datetime import datetime
from uuid import uuid4

import pytest

from app.adapters.repositories.repository import Repository
from app.core.entities.tournament import Tournament
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


@pytest.mark.parametrize(
    "payload, status_code",
    [
        [{"name": f"{uuid4()}"}, 422],
        [{"description": f"{uuid4()}"}, 422],
        [{"name": f"{uuid4()}", "description": f"{uuid4()}"}, 422],
        [{"name": f"{uuid4()}", "last_date_to_register": f"{datetime.now()}"}, 201],
        [{"name": f"{uuid4()}", "description": f"{uuid4()}", "last_date_to_register": f"{datetime.now()}"}, 201]
    ]
)
def test_create_tournament_properly_validate_input_data(test_app, monkeypatch, payload, status_code):
    async def mock_post(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "create", mock_post)

    response = test_app.post("/tournaments", data=json.dumps(payload))
    assert response.status_code == status_code


def test_read_tournament(test_app, monkeypatch):
    test_data = Tournament.create(**ATournamentDto().build().dict())

    async def mock_get(_self, _tournament_id):
        return test_data
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.get(f"/tournaments/{uuid4()}")
    assert response.status_code == 200
    assert response.json() == json.loads(test_data.json())


def test_read_tournament_incorrect_id(test_app, monkeypatch):
    async def mock_get(_self, _tournament_id):
        return None
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.get(f"/tournaments/{uuid4()}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tournament not found"


def test_update_tournament(test_app, monkeypatch):
    test_dto = ATournamentDto().build()
    test_data = Tournament.create(**test_dto.dict())

    async def mock_get(_self, _tournament_id):
        return test_data
    monkeypatch.setattr(Repository, "get", mock_get)

    async def mock_put(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "update", mock_put)

    response = test_app.put(f"/tournaments/{uuid4()}", data=test_dto.json())
    assert response.status_code == 200
    assert response.json() == json.loads(test_data.json())


@pytest.mark.parametrize(
    "payload, status_code",
    [
        [{"name": f"{uuid4()}"}, 422],
        [{"description": f"{uuid4()}"}, 422],
        [{"name": f"{uuid4()}", "description": f"{uuid4()}"}, 422],
        [{"name": f"{uuid4()}", "last_date_to_register": f"{datetime.now()}"}, 404],
        [{"name": f"{uuid4()}", "description": f"{uuid4()}", "last_date_to_register": f"{datetime.now()}"}, 404]
    ]
)
def test_update_tournament_invalid(test_app, monkeypatch, payload, status_code):
    async def mock_get(_self, _tournament_id):
        return None
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.put(f"/tournaments/{uuid4()}", data=json.dumps(payload))
    assert response.status_code == status_code


def test_delete_tournament(test_app, monkeypatch):
    test_data = Tournament.create(**ATournamentDto().build())

    async def mock_get(_self, _tournament_id):
        return test_data
    monkeypatch.setattr(Repository, "get", mock_get)

    async def mock_delete(_self, _tournament_id):
        pass
    monkeypatch.setattr(Repository, "delete", mock_delete)

    result = test_app.delete(f"/tournaments/{uuid4()}")
    assert result.status_code == 200
    assert result.json() == json.dumps(test_data.dict)


def test_delete_tournament_incorrect_id(test_app, monkeypatch):
    async def mock_get(_self, _tournament_id):
        return None
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.delete(f"/tournaments/{uuid4()}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tournament not found"
