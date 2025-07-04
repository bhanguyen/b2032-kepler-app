import duckdb
import os
from contextlib import contextmanager
from typing import List, Dict, Any, Optional

@contextmanager
def get_database_connection(db_path: Optional[str] = None):
    """Context manager for database connections to ensure proper cleanup."""
    if db_path is None:
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

def connect_to_database(db_path: str):
    """Legacy function maintained for backward compatibility."""
    import duckdb
    return duckdb.connect(db_path)

def fetch_geospatial_data(connection=None, db_path: Optional[str] = None) -> List[Any]:
    """Fetch geospatial data with proper connection management."""
    if connection is not None:
        # Use provided connection
        query = "SELECT * FROM sensor_readings"
        return connection.execute(query).fetchall()
    else:
        # Use context manager for connection
        with get_database_connection(db_path) as conn:
            query = "SELECT * FROM sensor_readings"
            return conn.execute(query).fetchall()

def process_data(data: List[Any]) -> List[Dict[str, Any]]:
    """Process raw database data into structured format with error handling."""
    try:
        processed_data = []
        for row in data:
            if len(row) >= 4:  # Ensure row has enough columns
                processed_data.append({
                    "id": row[0],
                    "latitude": row[1], 
                    "longitude": row[2], 
                    "value": row[3]
                })
        return processed_data
    except (IndexError, TypeError) as e:
        raise ValueError(f"Error processing data: {e}")

def get_sensor_readings(db_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """High-level function to get processed sensor readings."""
    raw_data = fetch_geospatial_data(db_path=db_path)
    return process_data(raw_data)