# Import necessary libraries
from fastapi import FastAPI, Query  # for creating a FastAPI web server
from sqlalchemy.types import String, Integer
from database.queries import insert_data, compute_metric, insert_metric_data, truncate_table
from utils.helpers import determine_table_name
from storage.blob_client import get_blob_client
from database.connection import get_db_connection, get_sqlalchemy_db_connection

app = FastAPI()

# API endpoint to truncate the data on all tables
@app.get("/truncate_table")
async def deleting_records(table_name: str):
    """First, truncate the data of each table in the Azure SQL database before using the following features. Try using jobs, departments, hired_employees, metric1 or metric2 name tables."""

    query = f"TRUNCATE TABLE {table_name}"
    try:
        with get_db_connection() as db_connection:
            truncate_response = truncate_table(query, table_name, db_connection)

        return truncate_response
    except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 400)
        return {"error": str(e)}

# API endpoint to retrieve CSV data and insert into SQL
@app.get("/csv/{filename}")
async def get_csv_data(filename: str):
    """Retrieves CSV data from Azure Blob Storage and inserts it into Azure SQL Database. Try with the jobs.csv, departments.csv and hired_employees.csv files"""

    try:
        # Download the CSV blob
        with get_blob_client() as container_client:
            blob_client = container_client.get_blob_client(filename)
            download_stream = blob_client.download_blob()
        
            # Read the CSV data from the download stream
            csv_data = download_stream.content_as_text(encoding="utf-8").splitlines()
            data = [row.split(",") for row in csv_data[0:]]

            # Determine table name and headers
            table_name, headers = determine_table_name(filename)

        # Insert data into SQL table
        with get_db_connection() as db_connection:
            response = insert_data(data, table_name, headers, db_connection)
        return response
    except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}

# API endpoints to compute the first metric
@app.get("/hired_by_quarter")
async def calculate_first_metric():
   """Shows the number of employees hired for each job and department in 2021 divided by quarter. This metric needs the inserted data of the 3 previous CSV files."""

   query = "SELECT d.department, j.job, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 1 AND 3 THEN 1 ELSE 0 END) AS Q1, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 4 AND 6 THEN 1 ELSE 0 END) AS Q2, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 7 AND 9 THEN 1 ELSE 0 END) AS Q3, SUM(CASE WHEN MONTH(h.datetime) BETWEEN 10 AND 12 THEN 1 ELSE 0 END) AS Q4 FROM hired_employees h INNER JOIN departments d ON d.id = h.department_id INNER JOIN jobs j ON j.id = h.job_id WHERE YEAR(h.datetime) = '2021' GROUP BY d.department, j.job ORDER BY d.department, j.job"

   try:
      with get_db_connection() as db_connection:
          data_response = compute_metric(query, db_connection)
    
      conn = get_sqlalchemy_db_connection()
      insert_response = insert_metric_data(result_api=data_response,table_name='metric1', dtype_cols={"department": String(), "job": String(), "Q1": Integer(),"Q2": Integer(),"Q3": Integer(),"Q4": Integer()}, engine=conn)
      
      return data_response, insert_response
   except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}

# API endpoints to compute the second metric
@app.get("/most_hired_in_2021")
async def calculate_second_metric():
   """Shows which departments hired more employees than the mean of employees hired in 2021 of all departments. This metric needs the inserted data of hired_employees and departments CSV files."""

   query = "WITH contratados_2021 AS (SELECT d.id,  d.department, COUNT(h.id) AS hired FROM hired_employees h INNER JOIN departments d ON d.id = h.department_id WHERE YEAR(h.datetime) = '2021' GROUP BY d.id, d.department) SELECT  d.id,  d.department, COUNT(h.id) AS hired FROM hired_employees h INNER JOIN departments d ON d.id = h.department_id GROUP BY d.id, d.department HAVING COUNT(h.id) > (SELECT AVG(hired) AS promedio FROM contratados_2021) ORDER BY hired DESC"

   try:
      with get_db_connection() as db_connection:
          data_response = compute_metric(query, db_connection)
    
      conn = get_sqlalchemy_db_connection()
      insert_response = insert_metric_data(result_api=data_response,table_name='metric2', dtype_cols={"id": Integer(), "department": String(), "hired": Integer()}, engine=conn)
      
      return data_response, insert_response
   except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
