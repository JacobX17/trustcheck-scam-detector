import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def test_user():
    return {
        "email": "test@example.com",
        "username": "testuser",
        "password": "SecurePass123!"
    }

def test_register_user(test_user):
    response = client.post("/api/v1/auth/register", json=test_user)
    assert response.status_code == 200

def test_login_user(test_user):
    client.post("/api/v1/auth/register", json=test_user)
    response = client.post(
        "/api/v1/auth/login",
        json={"email": test_user["email"], "password": test_user["password"]}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
