import json
import pytest

from tests.arrangers.an_user_dto import AnUserDto


# TO REFACTOR
@pytest.mark.integration
def test_create_user(test_app):
    test_user = AnUserDto().build()

    response = test_app.post("/users", data=test_user.json())

    assert response.status_code == 201
    expected_user = response.json()
    assert expected_user["username"] == test_user.username
    assert expected_user["password"] == test_user.password
    assert expected_user["email"] == test_user.email
