from fastapi import APIRouter
from app.db.mongo import points_collection, polygons_collection

router = APIRouter()
@router.post("/load-sample-data")
@router.get("/load-sample-data")
def load_sample_data():
    points_collection.delete_many({})
    polygons_collection.delete_many({})

    points = [
        {
            "name": "Connaught Place",
            "location": { "type": "Point", "coordinates": [77.2195, 28.6315] },
            "metadata": { "category": "market", "city": "Delhi" }
        },
        {
            "name": "India Gate",
            "location": { "type": "Point", "coordinates": [77.2295, 28.6129] },
            "metadata": { "category": "monument", "built": 1931 }
        },
        {
            "name": "Qutub Minar",
            "location": { "type": "Point", "coordinates": [77.1855, 28.5244] },
            "metadata": { "category": "UNESCO site", "height_m": 72.5 }
        }
    ]

    polygons = [
        {
            "name": "Central Delhi",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [77.2100, 28.6200],
                    [77.2400, 28.6200],
                    [77.2400, 28.6400],
                    [77.2100, 28.6400],
                    [77.2100, 28.6200]
                ]]
            },
            "metadata": { "zone": "administrative", "priority": "high" }
        },
        {
            "name": "South-Central Delhi",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [77.1700, 28.5100],
                    [77.2500, 28.5100],
                    [77.2500, 28.6500],
                    [77.1700, 28.6500],
                    [77.1700, 28.5100]
                ]]
            },
            "metadata": { "zone": "extended-area" }
        }
    ]

    points_collection.insert_many(points)
    polygons_collection.insert_many(polygons)

    return {
        "message": "Sample data loaded with metadata",
        "points": len(points),
        "polygons": len(polygons)
    }
