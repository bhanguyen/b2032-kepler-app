def connect_to_database(db_path: str):
    import duckdb
    return duckdb.connect(db_path)

def fetch_geospatial_data(connection):
    query = "SELECT * FROM sensor_readings"
    return connection.execute(query).fetchall()

def process_data(data):
    # Example processing function that could be expanded
    return [{"latitude": row[1], "longitude": row[2], "value": row[3]} for row in data]