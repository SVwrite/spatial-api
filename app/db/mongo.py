from pymongo import MongoClient
from dotenv import load_dotenv
from ..core.config import settings
import os

load_dotenv()

MONGO_URI = settings.MONGO_URI
MONGO_DB = settings.MONGO_DB

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

# Access collections
points_collection = db["points"]
polygons_collection = db["polygons"]
