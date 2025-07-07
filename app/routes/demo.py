from fastapi import APIRouter
from app.db.mongo import points_collection, polygons_collection

router = APIRouter()

@router.post("/load-sample-data")
@router.get("/load-sample-data")
def load_sample_data():
    # Clear existing
    points_collection.delete_many({})
    polygons_collection.delete_many({})

    # Insert points
    points = [
        { "name": "Connaught Place", "location": { "type": "Point", "coordinates": [77.2195, 28.6315] } },
        { "name": "India Gate",       "location": { "type": "Point", "coordinates": [77.2295, 28.6129] } },
        { "name": "Qutub Minar",      "location": { "type": "Point", "coordinates": [77.1855, 28.5244] } }
    ]

    polygons = [
        { "name": "Central Delhi", "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [77.2100, 28.6200],
                [77.2400, 28.6200],
                [77.2400, 28.6400],
                [77.2100, 28.6400],
                [77.2100, 28.6200]
            ]]
        }},
        { "name": "South-Central Delhi", "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [77.1700, 28.5100],
                [77.2500, 28.5100],
                [77.2500, 28.6500],
                [77.1700, 28.6500],
                [77.1700, 28.5100]
            ]]
        }}
    ]

    points_collection.insert_many(points)
    polygons_collection.insert_many(polygons)

    return {"message": "Sample data loaded", "points": len(points), "polygons": len(polygons)}
