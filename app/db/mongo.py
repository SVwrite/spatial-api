import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Explicitly load .env.test if running tests
if os.getenv("TESTING", "").lower() == "true":
    load_dotenv(dotenv_path=".env.test")
else:
    load_dotenv(dotenv_path=".env")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "spatialdb")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

points_collection = db["points"]
polygons_collection = db["polygons"]

# Avoid index creation error if MongoDB is unreachable
try:
    points_collection.create_index([("location", "2dsphere")])
    polygons_collection.create_index([("geometry", "2dsphere")])
except Exception as e:
    print(f"[⚠️ MongoDB Warning] Index creation failed: {e}")
