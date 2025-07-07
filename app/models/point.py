from pydantic import BaseModel
from typing import List, Literal, Optional, Dict

class Coordinates(BaseModel):
    type: Literal["Point"]
    coordinates: List[float]

class PointCreate(BaseModel):
    name: str
    location: Coordinates
    metadata: Optional[Dict] = {}

class PointOut(BaseModel):
    id: str
    name: str
    location: Coordinates
    metadata: Dict
