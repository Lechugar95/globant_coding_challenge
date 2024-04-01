# Import necessary libraries
from fastapi import FastAPI, Query  # for creating a FastAPI web server
from azure.storage.blob import BlobServiceClient  # for interacting with Azure Blob Storage
from database.connection import db_connection_string
from database.queries import insert_data, compute_metric
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
        #print(csv_data)
        data = [row.split(",") for row in csv_data[0:]]
        #print(data)

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
      response = compute_metric(query)
      return response
   except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}
   
@app.get("/most_hired_in_2021")
async def calculate_second_metric():
   """Shows which departments hired more employees than the mean of employees hired in 2021 of all departments."""

   query = "with empleados_2021 as (select d.id,  d.department, count(h.id) as empleados from hired_employees h inner join departments d on d.id = h.department_id where year(h.datetime) = '2021' group by d.id, d.department) select  d.id,  d.department, count(h.id) as empleados from hired_employees h inner join departments d on d.id = h.department_id group by d.id, d.department having count(h.id) > (select avg(empleados) as promedio from empleados_2021) order by empleados desc"

   try:
      response = compute_metric(query)
      return response
   except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

