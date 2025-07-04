import duckdb
import pandas as pd
import geopandas as gpd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

"""
This script generates a DuckDB database from a GeoJSON file.
It reads the GeoJSON file using GeoPandas and writes it to a DuckDB database.
Make sure to replace 'path_to_your_geojson_file.geojson' with the actual path to your GeoJSON file.
"""
DATA_DIR = os.getenv("DATA_DIR")
if not DATA_DIR:
    raise ValueError("DATA_DIR environment variable is not set. Please set it to the directory containing your data files.")
else:
    print(f"DATA_DIR is set to: {DATA_DIR}")

# Type check to satisfy linter - DATA_DIR is guaranteed to be a string here
assert isinstance(DATA_DIR, str), "DATA_DIR must be a string"

def generate_duckdb_data():
    # Create a DuckDB connection
    conn = duckdb.connect('my_geospatial_data.duckdb')

    try:
        # Load GeoJSON data - use environment variable for file path
        geojson_filename = os.getenv("GEOJSON_FILE", "sample_data.geojson")
        geojson_path = os.path.join(DATA_DIR, geojson_filename)
        
        if not os.path.exists(geojson_path):
            raise FileNotFoundError(f"GeoJSON file not found at: {geojson_path}")
        
        print(f"Loading GeoJSON data from: {geojson_path}")
        gdf = gpd.read_file(geojson_path)

        # Write GeoJSON data to DuckDB
        conn.execute("CREATE TABLE IF NOT EXISTS geojson_data AS SELECT * FROM gdf")
        print("Successfully created geojson_data table")

        # Create a sensor_readings table with sample data for the API
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sensor_readings AS
            SELECT 
                ROW_NUMBER() OVER () as id,
                ST_Y(geometry) as latitude,
                ST_X(geometry) as longitude,
                RANDOM() * 100 as value
            FROM geojson_data
            LIMIT 1000
        """)
        print("Successfully created sensor_readings table")

    except Exception as e:
        print(f"Error generating database: {e}")
        raise
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    generate_duckdb_data()