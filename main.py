# Import necessary libraries
from fastapi import FastAPI  # for creating a FastAPI web server
from azure.storage.blob import BlobServiceClient  # for interacting with Azure Blob Storage
from sqlalchemy.types import String, Integer
from database.queries import insert_data, compute_metric, insert_metric_data, truncate_table
from storage.blob_client import storage_connection_string, container_name
from utils.helpers import determine_table_name



app = FastAPI()

# API endpoint to retrieve CSV data and insert into SQL
@app.get("/csv/{filename}")
async def get_csv_data(filename: str):
    """Retrieves CSV data from Azure Blob Storage and inserts it into Azure SQL Database."""

    try:
        # Create BlobServiceClient and get the container client
        blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
        
        # Get a reference to the container
        container_client = blob_service_client.get_container_client(container_name)
        
        # Download the CSV blob
        blob_client = container_client.get_blob_client(filename)
        download_stream = blob_client.download_blob()
        
        # Read the CSV data from the download stream
        csv_data = download_stream.content_as_text(encoding="utf-8").splitlines()
        data = [row.split(",") for row in csv_data[0:]]

        # Determine table name and headers
        table_name, headers = determine_table_name(filename)

        # Insert data into SQL table
        response = insert_data(data, table_name, headers)
        return response
    except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}

@app.get("/hired_by_quarter")
async def calculate_first_metric():
   """Shows the number of employees hired for each job and department in 2021 divided by quarter."""

   query = "SELECT d.department, j.job, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 1 AND 3 THEN 1 ELSE 0 END) AS Q1, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 4 AND 6 THEN 1 ELSE 0 END) AS Q2, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 7 AND 9 THEN 1 ELSE 0 END) AS Q3, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 10 AND 12 THEN 1 ELSE 0 END) AS Q4 FROM hired_employees h INNER JOIN departments d ON d.id = h.department_id INNER JOIN jobs j ON j.id = h.job_id WHERE YEAR(h.datetime) = '2021' GROUP BY d.department, j.job ORDER BY d.department, j.job"

   try:
      data_response = compute_metric(query)
      
      insert_response = insert_metric_data(result_api=data_response,table_name='metric1', dtype_cols={"department": String(), "job": String(), "Q1": Integer(),"Q2": Integer(),"Q3": Integer(),"Q4": Integer()})

      return data_response, insert_response
   except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}
   
@app.get("/most_hired_in_2021")
async def calculate_second_metric():
   """Shows which departments hired more employees than the mean of employees hired in 2021 of all departments."""

   query = "WITH contratados_2021 AS (SELECT d.id,  d.department, COUNT(h.id) AS hired FROM hired_employees h INNER JOIN departments d ON d.id = h.department_id WHERE YEAR(h.datetime) = '2021' GROUP BY d.id, d.department) SELECT  d.id,  d.department, COUNT(h.id) AS hired FROM hired_employees h INNER JOIN departments d ON d.id = h.department_id GROUP BY d.id, d.department HAVING COUNT(h.id) > (SELECT AVG(hired) AS promedio FROM contratados_2021) ORDER BY hired DESC"

   try:
      data_response = compute_metric(query)
      insert_response = insert_metric_data(result_api=data_response,table_name='metric2', dtype_cols={"id": Integer(), "department": String(), "hired": Integer()})
      return data_response, insert_response
   except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}
   
@app.get("/truncate_table")
async def deleting_records(table_name: str):
    """Cleans the data of the specified table in the Azure SQL database."""

    query = f"TRUNCATE TABLE {table_name}"
    try:
        truncate_response = truncate_table(query, table_name)

        return truncate_response
    except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 400)
        return {"error": str(e)}


# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

