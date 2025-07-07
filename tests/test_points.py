import os
os.environ["TESTING"] = "true"

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.mongo import points_collection

client = TestClient(app)

# Shared across tests
test_point = {
    "name": "Gateway of India",
    "location": {
        "type": "Point",
        "coordinates": [72.8347, 18.9218]
    }
}

updated_point = {
    "name": "Updated Gateway",
    "location": {
        "type": "Point",
        "coordinates": [72.8350, 18.9220]
    }
}


@pytest.fixture(scope="module")
def clean_db():
    points_collection.delete_many({})  # clear all before testing
    yield
    points_collection.delete_many({})  # clean up after


def test_create_point(clean_db):
    response = client.post("/points", json=test_point)
    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["name"] == test_point["name"]
    assert data["location"]["type"] == "Point"
    assert data["location"]["coordinates"] == test_point["location"]["coordinates"]

    # store id for later use
    global point_id
    point_id = data["id"]


def test_get_all_points():
    response = client.get("/points")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1

    point = data[0]
    assert point["id"] == point_id
    assert point["name"] == test_point["name"]
    assert point["location"]["coordinates"] == test_point["location"]["coordinates"]


def test_put_point():
    response = client.put(f"/points/{point_id}", json=updated_point)
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == point_id
    assert data["name"] == updated_point["name"]
    assert data["location"]["coordinates"] == updated_point["location"]["coordinates"]


def test_patch_point():
    response = client.patch(f"/points/{point_id}", json={"name": "Partially Patched Name"})
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == point_id
    assert data["name"] == "Partially Patched Name"
    assert data["location"]["coordinates"] == updated_point["location"]["coordinates"]
