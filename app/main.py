from fastapi import FastAPI
from app.db.mongo import db
from app.db.mongo import points_collection, polygons_collection
# from app.routes import points, polygons

app = FastAPI(title="Spatial API")

# app.include_router(points.router, prefix="/points", tags=["Points"])
# app.include_router(polygons.router, prefix="/polygons", tags=["Polygons"])




@app.get("/ping-db")
def ping_db():
    return {"collections": db.list_collection_names()}




from app.routes import points
app.include_router(points.router, prefix="/points", tags=["Points"])


from app.routes import polygons
app.include_router(polygons.router, prefix="/polygons", tags=["Polygons"])

#
# @app.get("/init-db")
# def init_db():
#     points_collection.insert_one({
#         "name": "dummy_point",
#         "location": {
#             "type": "Point",
#             "coordinates": [77.2, 28.6]
#         }
#     })
#     polygons_collection.insert_one({
#         "name": "dummy_polygon",
#         "geometry": {
#             "type": "Polygon",
#             "coordinates": [[[77.2, 28.6], [77.3, 28.6], [77.3, 28.7], [77.2, 28.7], [77.2, 28.6]]]
#         }
#     })
#     return {"status": "inserted"}
