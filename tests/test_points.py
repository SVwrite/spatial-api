import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_point():
    response = client.post("/points", json={
        "name": "Test Point",
        "location": {
            "type": "Point",
            "coordinates": [77.25, 28.65]
        }
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Point"
    assert data["location"]["type"] == "Point"
    assert isinstance(data["location"]["coordinates"], list)

def test_get_points():
    response = client.get("/points")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
