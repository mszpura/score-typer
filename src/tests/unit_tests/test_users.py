import json
import uuid
import pytest
from app.adapters.repositories.repository import Repository
from app.core.entities.user import User
from tests.arrangers.an_user_dto import AnUserDto


def test_create_user(test_app, monkeypatch):
    test_user = AnUserDto().build()

    async def mock_post(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "create", mock_post)

    response = test_app.post("/users", data=test_user.json())
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None


def test_create_user_invalid_json(test_app):
    response = test_app.post("/users", data=json.dumps({"username": "idk"}))
    assert response.status_code == 422

    response = test_app.post("/users", data=json.dumps({"username": "123", "password": "456", "email": "email"}))
    assert response.status_code == 422


def test_read_user(test_app, monkeypatch):
    test_data = User.create(**AnUserDto().build().dict())

    async def mock_get(_self, user_id):
        return test_data
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.get(f"/users/{uuid.uuid4()}")
    assert response.status_code == 200
    assert response.json() == json.loads(test_data.json())


def test_read_user_incorrect_id(test_app, monkeypatch):
    async def mock_get(_self, _user_id):
        return None
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.get(f"/users/{uuid.uuid4()}")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_read_all_users(test_app, monkeypatch):
    user1 = User.create(**AnUserDto().build().dict())
    user2 = User.create(**AnUserDto().build().dict())

    async def mock_get_all(_self, ):
        return [user1, user2]
    monkeypatch.setattr(Repository, "get_all", mock_get_all)

    response = test_app.get("/users")
    assert response.status_code == 200


def test_update_user(test_app, monkeypatch):
    test_data = AnUserDto().build()
    test_result = User.create(**test_data.dict())

    async def mock_get(_self, _user_id):
        return test_result
    monkeypatch.setattr(Repository, "get", mock_get)

    async def mock_put(_self, _payload):
        pass
    monkeypatch.setattr(Repository, "update", mock_put)

    response = test_app.put(f"/users/{uuid.uuid4()}", data=test_data.json())
    assert response.status_code == 200
    assert response.json() == json.loads(test_result.json())


@pytest.mark.parametrize(
    "user_id, payload, status_code",
    [
        [uuid.UUID("0b9bd788-28b5-478b-9c27-adedcaf4a4b5"), {}, 422],
        [uuid.UUID("25e38201-c2e2-41ba-adc2-aea413d70d94"), {"username": "monika"}, 422],
        [uuid.UUID("30d33288-d980-4804-90cc-993964a11893"), {"username": "magda", "password": "dunno", "email": "test_email@gmail.com"}, 404],
        [uuid.UUID("30d33288-d980-4804-90cc-993964a11893"), {"username": "123", "password": "1235678", "email": "szpura.maciej@gmail.com"}, 422],
        [uuid.UUID("30d33288-d980-4804-90cc-993964a11893"), {"username": "maciek", "password": "123", "email": "szpura.maciej@gmail.com"}, 422],
        [uuid.UUID("30d33288-d980-4804-90cc-993964a11893"), {"username": "maciek", "password": "hasło_hasło", "email": "qwe"}, 422],
    ]
)
def test_update_user_invalid(test_app, monkeypatch, user_id, payload, status_code):
    async def mock_get(_self, _user_id):
        return None
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.put(f"/users/{user_id}", data=json.dumps(payload),)
    assert response.status_code == status_code


def test_remove_user(test_app, monkeypatch):
    test_data = User.create(**AnUserDto().build().dict())

    async def mock_get(_self, _user_id):
        return test_data
    monkeypatch.setattr(Repository, "get", mock_get)

    async def mock_delete(_self, _user_id):
        pass
    monkeypatch.setattr(Repository, "delete", mock_delete)

    response = test_app.delete(f"/users/{uuid.uuid4()}")
    assert response.status_code == 200
    assert response.json() == json.loads(test_data.json())


def test_remove_user_incorrect_id(test_app, monkeypatch):
    async def mock_get(_self, _user_id):
        return None
    monkeypatch.setattr(Repository, "get", mock_get)

    response = test_app.delete(f"/users/{uuid.uuid4()}")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
