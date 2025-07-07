from pydantic import BaseModel
from typing import List, Literal, Optional, Dict

class PolygonGeometry(BaseModel):
    type: Literal["Polygon"]
    coordinates: List[List[List[float]]]

class PolygonCreate(BaseModel):
    name: str
    geometry: PolygonGeometry
    metadata: Optional[Dict] = {}

class PolygonOut(BaseModel):
    id: str
    name: str
    geometry: PolygonGeometry
    metadata: Dict
