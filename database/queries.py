import pyodbc
from database.connection import db_connection_string

def insert_data(data, table_name, headers):
  """Inserts data into the specified table in Azure SQL Database."""
  # Construct the INSERT query with placeholders for values
  column_placeholders = ", ".join(["?"] * len(headers))
  insert_query = f"INSERT INTO {table_name} ({','.join(headers)}) VALUES ({column_placeholders})"
  #print(insert_query)
  
  try:
    with pyodbc.connect(db_connection_string) as conn:
      with conn.cursor() as cursor:
        for row in data:
          #print(row)
          cursor.execute(insert_query, row)  # Execute the query with each row
        conn.commit()  # Commit the changes
    return {"message": "Data inserted successfully!"}
  except Exception as e:
    return {"error": str(e)}  # Return an error message if any exception occurs

def compute_metric(query):
   """Lists the number of employees hired for each job and department in 2021 divided by quarter using SQL."""

   try:
      with pyodbc.connect(db_connection_string) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)  # Execute the query with each row
            results = cursor.fetchall()
      metric_results = [dict(zip([col[0] for col in cursor.description], row)) for row in results]

      return {"message": "Metric computed successfully!", "data": metric_results}
   
   except Exception as e:
      return {"error": str(e)}  # Return an error message if any exception occurs
