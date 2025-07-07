from fastapi import APIRouter, HTTPException
from app.db.mongo import points_collection, polygons_collection

router = APIRouter()

@router.post("/points-in-polygon")
def get_points_in_polygon(polygon: dict):
    if "type" not in polygon or polygon["type"] != "Polygon":
        raise HTTPException(status_code=400, detail="Invalid GeoJSON Polygon")

    query = {
        "location": {
            "$geoWithin": {
                "$geometry": polygon
            }
        }
    }

    results = list(points_collection.find(query))
    return [
        {
            "id": str(p["_id"]),
            "name": p["name"],
            "location": p["location"]
        } for p in results
    ]


@router.post("/polygons-containing-point")
def get_polygons_containing_point(point: dict):
    if "type" not in point or point["type"] != "Point":
        raise HTTPException(status_code=400, detail="Invalid GeoJSON Point")

    query = {
        "geometry": {
            "$geoIntersects": {
                "$geometry": point
            }
        }
    }

    results = list(polygons_collection.find(query))
    return [
        {
            "id": str(p["_id"]),
            "name": p["name"],
            "geometry": p["geometry"]
        } for p in results
    ]
