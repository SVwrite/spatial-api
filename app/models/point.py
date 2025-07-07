from pydantic import BaseModel, Field
from typing import List, Literal

class Coordinates(BaseModel):
    type: Literal["Point"] = "Point"
    coordinates: List[float]  # [lng, lat]

class PointCreate(BaseModel):
    name: str
    location: Coordinates

class PointOut(BaseModel):
    id: str
    name: str
    location: Coordinates
