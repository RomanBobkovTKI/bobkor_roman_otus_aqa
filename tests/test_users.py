from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_user():
    response = client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "age" in data
    assert "job" in data