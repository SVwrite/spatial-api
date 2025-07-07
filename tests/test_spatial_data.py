import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_points_within_polygon():
    client.get("/demo/load-sample-data")

    polygon = {
        "type": "Polygon",
        "coordinates": [[
            [77.1700, 28.5100],
            [77.2500, 28.5100],
            [77.2500, 28.6500],
            [77.1700, 28.6500],
            [77.1700, 28.5100]
        ]]
    }

    response = client.post("/spatial/points-in-polygon", json=polygon)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert any(p["name"] == "India Gate" for p in data)
    assert any(p["name"] == "Qutub Minar" for p in data)


def test_polygons_containing_point():
    point = {
        "type": "Point",
        "coordinates": [77.2195, 28.6315]  # Connaught Place
    }

    response = client.post("/spatial/polygons-containing-point", json=point)
    assert response.status_code == 200
    data = response.json()
    names = [p["name"] for p in data]
    assert "Central Delhi" in names
    assert "South-Central Delhi" in names
