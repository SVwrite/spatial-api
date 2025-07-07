from pydantic import BaseModel
from typing import List, Literal

class PolygonGeometry(BaseModel):
    type: Literal["Polygon"]
    coordinates: List[List[List[float]]]  # List of Linear Rings: [[[lng, lat], [lng, lat], ...]]

class PolygonCreate(BaseModel):
    name: str
    geometry: PolygonGeometry

class PolygonOut(BaseModel):
    id: str
    name: str
    geometry: PolygonGeometry
