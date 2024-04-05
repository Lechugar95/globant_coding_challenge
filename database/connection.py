# Connection string for Azure resource. Replace them with your connection string
# For the azure sql database
#pyodbc_db_con_string = "YOUR_AZURE_SQL_DATABASE_CONNECTION_STRING_FOR_PYODBC"

# Uncomment and try with the following connection string. Don't forget to comment the line above of connection string.
pyodbc_db_con_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:servermigration1.database.windows.net,1433;Database=databasemigration1;Uid=admin_migration;Pwd=CLOUDgcp#246;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

# For the azure sql database
#salchemy_db_con_string = "YOUR_AZURE_SQL_DATABASE_CONNECTION_STRING_FOR_SQLALCHEMY"

# Uncomment and try with the following connection string. Don't forget to comment the line above of connection string.
salchemy_db_con_string = "mssql+pyodbc://admin_migration:CLOUDgcp#246@servermigration1.database.windows.net:1433/databasemigration1?driver=ODBC+Driver+17+for+SQL+Server"
