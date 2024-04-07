import pyodbc
import pandas as pd
import sqlalchemy as sa
from database.connection import pyodbc_db_con_string, salchemy_db_con_string

def insert_data(data, table_name, headers):
  """Inserts data into the specified table in Azure SQL Database."""
  # Construct the INSERT query with placeholders for values
  column_placeholders = ", ".join(["?"] * len(headers))
  insert_query = f"INSERT INTO {table_name} ({','.join(headers)}) VALUES ({column_placeholders})"
  
  try:
    with pyodbc.connect(pyodbc_db_con_string) as conn:
      with conn.cursor() as cursor:
        for row in data:
          cursor.execute(insert_query, row)  # Execute the query with each row
        conn.commit()  # Commit the changes

    return {"message": f"Data was inserted successfully into the {table_name} Azure SQL table!"}
  
  except Exception as e:

    return {"error": str(e)}  # Return an error message if any exception occurs

def compute_metric(query):
   """Lists the number of employees hired for each job and department in 2021 divided by quarter using SQL."""

   try:
      with pyodbc.connect(pyodbc_db_con_string) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
      metric_results = [dict(zip([col[0] for col in cursor.description], row)) for row in results]

      return {"message": "Metric computed successfully!", "data": metric_results}
      #return {"message": "Metric computed successfully!"}
   
   except Exception as e:
      
      return {"error": str(e)}  # Return an error message if any exception occurs

def insert_metric_data(result_api, table_name, dtype_cols):
  """Inserts the data in a Azure SQL table of the metrics obtained by the REST API."""
  try:
    metric_df = pd.json_normalize(result_api, 'data')
    engine = sa.create_engine(salchemy_db_con_string)
    metric_df.to_sql(name=table_name, con=engine, index=False, dtype=dtype_cols, if_exists='replace')

    return {"message": f"Metric data inserted successfully into the {table_name} Azure SQL table!"}
  
  except Exception as e:
    return {"error": str(e)}  # Return an error message if any exception occurs
  

def truncate_table(query, table_name):
  """Cleans the date of the specific table"""
  
  try:
     with pyodbc.connect(pyodbc_db_con_string) as conn:
       with conn.cursor() as cursor:
           cursor.execute(query)

     return {"message": f"{table_name} table was cleaned succesfully!"}
  
  except Exception as e:
     return {"error": str(e)}  # Return an error message if any exception occurs
