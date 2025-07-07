# Spatial API-FastAPI + MongoDB GeoJSON Platform

This is a spatial backend service built with **FastAPI** and **MongoDB**, supporting:
- Storing and querying **GeoJSON points** and **polygons**
- Running **spatial queries** such as:
  - Points within a polygon
  - Polygons that contain a point

---

## Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/spatial-api.git
cd spatial-api
```

### 2. Start the App with Docker

```bash
docker-compose up --build
```

This will start:
- FastAPI backend on [http://localhost:8000](http://localhost:8000)
- MongoDB with preconfigured network

---

## API Docs

Once running, explore all endpoints at:

```
http://localhost:8000/docs
```

This includes routes for:
- `/points`
- `/polygons`
- `/spatial`
- `/demo`

---

## API Summary

| Method | Route                                     | Description                       |
|--------|-------------------------------------------|-----------------------------------|
| POST   | `/points`                                 | Add a point                       |
| PUT    | `/points/{id}`                            | Replace a point                   |
| PATCH  | `/points/{id}`                            | Partially update a point          |
| GET    | `/points`                                 | List all points                   |
| POST   | `/points/bulk`                            | Bulk insert points                |
| POST   | `/polygons`                               | Add a polygon                     |
| PUT    | `/polygons/{id}`                          | Replace a polygon                 |
| PATCH  | `/polygons/{id}`                          | Partially update a polygon        |
| GET    | `/polygons`                               | List all polygons                 |
| POST   | `/spatial/points-in-polygon`              | Find points inside a polygon      |
| POST   | `/spatial/polygons-containing-point`      | Find polygons containing a point  |
| GET/POST | `/demo/load-sample-data`                | Insert known test data            |

---

## Running Tests

Tests use the MongoDB via `.env.test`.

### Setup
Create `.env.test`:
```env
MONGO_URI=mongodb://localhost:27017
MONGO_DB=spatialdb
```

### Run tests:

```bash
PYTHONPATH=. pytest
```

Tests are located in the `tests/` folder and cover:
- Points CRUD
- Spatial queries
- Polygon containment

---


## Load Sample Data

You can auto-load test data using this GET or POST:

```
GET http://localhost:8000/demo/load-sample-data
```

This will insert:

### Points:
| Name             | Coordinates              | Metadata                          |
|------------------|--------------------------|-----------------------------------|
| Connaught Place  | [77.2195, 28.6315]       | `{"category": "market"}`          |
| India Gate       | [77.2295, 28.6129]       | `{"category": "monument"}`        |
| Qutub Minar      | [77.1855, 28.5244]       | `{"category": "UNESCO site"}`     |

### Polygons:
| Name                | Description                          | Metadata                          |
|---------------------|--------------------------------------|-----------------------------------|
| Central Delhi       | Rectangle around Connaught Place     | `{"zone": "administrative"}`      |
| South-Central Delhi | Larger region including all 3 points | `{"zone": "extended-area"}`       |
---

## Spatial Query Examples

### Query 1: Points Within a Polygon

**Endpoint:**
```http
POST /spatial/points-in-polygon
```

**Body:**
```json
{
  "type": "Polygon",
  "coordinates": [[
    [77.1700, 28.5100],
    [77.2500, 28.5100],
    [77.2500, 28.6500],
    [77.1700, 28.6500],
    [77.1700, 28.5100]
  ]]
}
```

**Expected Result:** All 3 points returned (within the bounding box)

---

### Query 2: Polygons Containing a Point

**Endpoint:**
```http
POST /spatial/polygons-containing-point
```

**Body:**
```json
{
  "type": "Point",
  "coordinates": [77.2195, 28.6315]
}
```

**Expected Result:** Central Delhi and South-Central Delhi

---



## For Contributors

Fork the repo, and run locally using Docker Compose:

```bash
docker-compose up --build
```

Add your `.env` if needed - defaults are provided.

---

## Tech Stack

- **FastAPI** - Python web framework
- **MongoDB** - Document store with 2dsphere geospatial indexing
- **PyMongo** - Native MongoDB driver
- **Pydantic v2** - Schema validation
- **Docker & Compose** - Container orchestration
- **pytest** - Testing framework

---

## Contact

Maintained by Shreyansh Vatsyayan.  
If you're testing this for a project/assessment, just hit `/demo/load-sample-data` and start exploring.
