import json
import pytest
from app.adapters.postgres_repository.users_repo import UsersRepository
from tests.arrangers.an_user_dto import AnUserDto


def test_create_user(test_app, monkeypatch):
    test_user = AnUserDto().build().dict()

    async def mock_post(_self, _payload):
        pass
    monkeypatch.setattr(UsersRepository, "create", mock_post)

    response = test_app.post("/users", data=json.dumps(test_user))
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None


def test_create_user_invalid_json(test_app):
    response = test_app.post("/users", data=json.dumps({"username": "idk"}))
    assert response.status_code == 422

    response = test_app.post("/users", data=json.dumps({"username": "123", "password": "456", "email": "email"}))
    assert response.status_code == 422

#
# def test_read_user(test_app, monkeypatch):
#     test_data = {
#         "id": 1,
#         "username": "michal",
#         "password": "some_password",
#         "email": "michal.kalita@gmail.com"
#     }
#
#     async def mock_get(_user_id):
#         return test_data
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     response = test_app.get("/users/1")
#     assert response.status_code == 200
#     assert response.json() == test_data
#
#
# def test_read_user_incorrect_id(test_app, monkeypatch):
#     async def mock_get(_user_id):
#         return None
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     response = test_app.get("/users/999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "User not found"
#
#     response = test_app.get("/users/0")
#     assert response.status_code == 422
#
#
# def test_read_all_users(test_app, monkeypatch):
#     test_data = [
#         {"id": 1, "username": "michal_kalita", "password": "some_password", "email": "michal.kalita@gmail.com"},
#         {"id": 2, "username": "anna_szpura", "password": "qwertyrootqwerty", "email": "anna.szpura@onet.pl"}
#     ]
#
#     async def mock_get():
#         return test_data
#     monkeypatch.setattr(crud, "get_all", mock_get)
#
#     response = test_app.get("/users")
#     assert response.status_code == 200
#     assert response.json() == test_data
#
#
# def test_update_user(test_app, monkeypatch):
#     test_update_data = {
#         "id": 1,
#         "username": "michal",
#         "password": "some_password",
#         "email": "michal.kalita@gmail.com"
#     }
#
#     async def mock_get(_user_id):
#         return True
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     async def mock_put(_user_id, _payload):
#         return 1
#     monkeypatch.setattr(crud, "put", mock_put)
#
#     response = test_app.put("/users/1", data=json.dumps(test_update_data))
#     assert response.status_code == 200
#     assert response.json() == test_update_data
#
#
# @pytest.mark.parametrize(
#     "user_id, payload, status_code",
#     [
#         [1, {}, 422],
#         [1, {"username": "monika"}, 422],
#         [999, {"username": "magda", "password": "dunno", "email": "test_email@gmail.com"}, 404],
#         [1, {"username": "123", "password": "1235678", "email": "szpura.maciej@gmail.com"}, 422],
#         [1, {"username": "maciek", "password": "123", "email": "szpura.maciej@gmail.com"}, 422],
#         [1, {"username": "maciek", "password": "hasło_hasło", "email": "qwe"}, 422],
#         [0, {"username": "maciek", "password": "hasło_hasło", "email": "szpura.maciej@gmail.com"}, 422],
#     ]
# )
# def test_update_user_invalid(test_app, monkeypatch, user_id, payload, status_code):
#     async def mock_get(_user_id):
#         return None
#
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     response = test_app.put(f"/users/{user_id}", data=json.dumps(payload),)
#     assert response.status_code == status_code
#
#
# def test_remove_user(test_app, monkeypatch):
#     test_data = {"id": 1, "username": "michal_kalita", "password": "some_password", "email": "michal.kalita@gmail.com"}
#
#     async def mock_get(_user_id):
#         return test_data
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     async def mock_delete(user_id):
#         return user_id
#     monkeypatch.setattr(crud, "delete", mock_delete)
#
#     response = test_app.delete("/users/1")
#     assert response.status_code == 200
#     assert response.json() == test_data
#
#
# def test_remove_user_incorrect_id(test_app, monkeypatch):
#     async def mock_get(_user_id):
#         return None
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     response = test_app.delete("/users/999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "User not found"
#
#     response = test_app.delete("/users/0")
#     assert response.status_code == 422
