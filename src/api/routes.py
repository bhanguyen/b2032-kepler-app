from fastapi import APIRouter
import duckdb
from typing import List, Dict

router = APIRouter()

@router.get("/data/sensor_readings", response_model=List[Dict])
async def get_data():
    conn = duckdb.connect("my_geospatial_data.duckdb")
    query = "SELECT * FROM sensor_readings"
    result = conn.execute(query).fetchall()
    conn.close()
    return [{"id": row[0], "latitude": row[1], "longitude": row[2], "value": row[3]} for row in result]