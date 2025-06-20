import duckdb
import pandas as pd
import geopandas as gpd
from dotenv import load_env
import os

# Load environment variables from .env file
load_env()

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

def generate_duckdb_data():
    # Create a DuckDB connection
    conn = duckdb.connect('my_geospatial_data.duckdb')

    # Load GeoJSON data
    geojson_path = 'path_to_your_geojson_file.geojson'  # Replace with your GeoJSON file path
    gdf = gpd.read_file(geojson_path)

    # Write GeoJSON data to DuckDB
    conn.execute("CREATE TABLE geojson_data AS SELECT * FROM gdf")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    generate_duckdb_data()