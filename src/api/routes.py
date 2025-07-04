from fastapi import APIRouter, HTTPException
import duckdb
import os
from typing import List, Dict
from contextlib import contextmanager

router = APIRouter()

@contextmanager
def get_db_connection():
    """Context manager for database connections to ensure proper cleanup."""
    db_path = os.getenv("DATABASE_PATH", "my_geospatial_data.duckdb")
    conn = None
    try:
        conn = duckdb.connect(db_path)
        yield conn
    except Exception as e:
        if conn:
            conn.close()
        raise e
    finally:
        if conn:
            conn.close()

@router.get("/data/sensor_readings", response_model=List[Dict])
async def get_data():
    """Get sensor readings from the database with proper error handling."""
    try:
        with get_db_connection() as conn:
            query = "SELECT * FROM sensor_readings"
            result = conn.execute(query).fetchall()
            return [{"id": row[0], "latitude": row[1], "longitude": row[2], "value": row[3]} for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")