from fastapi import FastAPI, Query
from azure.storage.blob import BlobServiceClient
from pydantic import BaseModel
import pyodbc
  
db_connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:servermigration1.database.windows.net,1433;Database=databasemigration1;Uid=admin_migration;Pwd=CLOUDgcp#246;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

# Replace with your connection string
storage_connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"

# Container name where your CSV files are stored
container_name = "YOUR_CONTAINER_NAME"

app = FastAPI()

def determine_table_name(filename):
    # Implement logic to map filenames to table names
    # Example:
    #print(filename)
    if filename.startswith("departments"):
        table_name = "departments"
        headers = ['id','department']
        return table_name, headers
    elif filename.startswith("hired_employees"):
        table_name = "hired_employees"
        headers = ['id','name','datetime','department_id','job_id']
        return table_name, headers
    elif filename.startswith("jobs"):
        table_name = "jobs"
        headers = ['id','job']
        return table_name, headers
    else:
        raise ValueError(f"Invalid filename: {filename}")

def insert_data(data, table_name, headers):
  """Inserts data into the specified table in Azure SQL Database."""
  # Replace with your table name and column placeholders
  #table_name = "dbo.departments"
  column_placeholders = ", ".join(["?"] * len(headers))
  insert_query = f"INSERT INTO {table_name} ({','.join(headers)}) VALUES ({column_placeholders})"
  #print(insert_query)
  
  try:
    with pyodbc.connect(db_connection_string) as conn:
      with conn.cursor() as cursor:
        for row in data:
          #print(row)
          cursor.execute(insert_query, row)
        conn.commit()
    return {"message": "Data inserted successfully!"}
  except Exception as e:
    return {"error": str(e)}

class CSVData(BaseModel):
    headers: list[str]
    data: list[list[str]]

@app.get("/csv/{filename}")
async def get_csv_data(filename: str):
    try:
        # Create BlobServiceClient with the connection string
        blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
        
        # Get a reference to the container
        container_client = blob_service_client.get_container_client(container_name)
        
        # Download the specific CSV blob
        blob_client = container_client.get_blob_client(filename)
        download_stream = blob_client.download_blob()  # No need to await here
        
        # Read the CSV data from the download stream
        csv_data = download_stream.content_as_text(encoding="utf-8").splitlines()
        #print(csv_data)
        data = [row.split(",") for row in csv_data[0:]]
        #print(data)

        table_name, headers = determine_table_name(filename)

        # Insert data into SQL table
        response = insert_data(data, table_name, headers)
        return response
    except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)