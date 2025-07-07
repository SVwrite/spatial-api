from fastapi import APIRouter, HTTPException, Body
from bson import ObjectId
from app.db.mongo import polygons_collection
from app.models.polygon import PolygonCreate, PolygonOut

router = APIRouter()

def serialize_polygon(doc) -> dict:
    return {
        "id": str(doc["_id"]),
        "name": doc["name"],
        "geometry": doc["geometry"],
        "metadata": doc.get("metadata", {})
    }

@router.post("/", response_model=PolygonOut)
def add_polygon(polygon: PolygonCreate):
    result = polygons_collection.insert_one(polygon.dict())
    new_polygon = polygons_collection.find_one({"_id": result.inserted_id})
    return serialize_polygon(new_polygon)

@router.get("/", response_model=list[PolygonOut])
def get_all_polygons():
    polygons = polygons_collection.find()
    return [serialize_polygon(p) for p in polygons]

@router.put("/{polygon_id}", response_model=PolygonOut)
def update_polygon(polygon_id: str, polygon: PolygonCreate):
    result = polygons_collection.update_one(
        {"_id": ObjectId(polygon_id)},
        {"$set": polygon.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Polygon not found")
    updated = polygons_collection.find_one({"_id": ObjectId(polygon_id)})
    return serialize_polygon(updated)


@router.patch("/{polygon_id}", response_model=PolygonOut)
def patch_polygon(polygon_id: str, data: dict = Body(...)):
    result = polygons_collection.update_one(
        {"_id": ObjectId(polygon_id)},
        {"$set": data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Polygon not found")
    updated = polygons_collection.find_one({"_id": ObjectId(polygon_id)})
    return serialize_polygon(updated)
