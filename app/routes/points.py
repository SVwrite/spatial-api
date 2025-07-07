from fastapi import APIRouter, HTTPException, Body
from bson import ObjectId
from app.db.mongo import points_collection
from app.models.point import PointCreate, PointOut

router = APIRouter()

# Helper to convert MongoDB ObjectId
def serialize_point(doc) -> dict:
    return {
        "id": str(doc["_id"]),
        "name": doc["name"],
        "location": doc["location"]
    }

@router.post("/", response_model=PointOut)
def add_point(point: PointCreate):
    result = points_collection.insert_one(point.model_dump())
    new_point = points_collection.find_one({"_id": result.inserted_id})
    return serialize_point(new_point)

@router.get("/", response_model=list[PointOut])
def get_all_points():
    points = points_collection.find()
    return [serialize_point(p) for p in points]

@router.put("/{point_id}", response_model=PointOut)
def update_point(point_id: str, point: PointCreate):
    result = points_collection.update_one(
        {"_id": ObjectId(point_id)},
        {"$set": point.model_dump()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Point not found")
    updated = points_collection.find_one({"_id": ObjectId(point_id)})
    return serialize_point(updated)


@router.patch("/{point_id}", response_model=PointOut)
def patch_point(point_id: str, data: dict = Body(...)):
    result = points_collection.update_one(
        {"_id": ObjectId(point_id)},
        {"$set": data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Point not found")
    updated = points_collection.find_one({"_id": ObjectId(point_id)})
    return serialize_point(updated)
