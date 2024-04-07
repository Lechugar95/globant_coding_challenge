import pyodbc
import sqlalchemy as sa
from config import pyodbc_db_con_string, salchemy_db_con_string

def get_db_connection():
    """Establishes a connection to the Azure SQL Database."""
    try:
        conn = pyodbc.connect(pyodbc_db_con_string)
        return conn
    except Exception as e:
        raise ValueError("Error connecting to database:", e)

def get_sqlalchemy_db_connection():
    """Establishes a connection to the Azure SQL Database."""
    try:
        engine = sa.create_engine(salchemy_db_con_string)
        return engine
    except Exception as e:
        raise ValueError("Error connecting to database:", e)
