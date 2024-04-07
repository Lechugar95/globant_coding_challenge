# Connection string for Azure resources. Replace them with your connection string
# For the azure sql database
#pyodbc_db_con_string = "YOUR_AZURE_SQL_DATABASE_CONNECTION_STRING_FOR_PYODBC"

# Uncomment and try with the following connection string. Don't forget to comment the line above of connection string.
pyodbc_db_con_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:servermigration1.database.windows.net,1433;Database=databasemigration1;Uid=admin_migration;Pwd=CLOUDgcp#246;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

# For the azure sql database
#salchemy_db_con_string = "YOUR_AZURE_SQL_DATABASE_CONNECTION_STRING_FOR_SQLALCHEMY"

# Uncomment and try with the following connection string. Don't forget to comment the line above of connection string.
salchemy_db_con_string = "mssql+pyodbc://admin_migration:CLOUDgcp#246@servermigration1.database.windows.net:1433/databasemigration1?driver=ODBC+Driver+17+for+SQL+Server"

# Connection strings for Azure resources. Replace them with your connection strings
# For the blob storage
#storage_connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"

# Uncomment and try with the following connection string. Don't forget to comment the line above of connection string.
storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=inputapifiles;AccountKey=2hpa2I2Ks9j6yBQDdxeTAHtOJDpyqEQxzBvf7GBbwCbE9ZDu8w6vmTffCRiq8lVwlaWk4HQSP5Vt+AStNZ26Nw==;EndpointSuffix=core.windows.net"

# Container name where your CSV files are stored
#container_name = "YOUR_CONTAINER_NAME"

# Uncomment and try with the following container name. Don't forget to comment the line above of container name.
container_name = "apifiles/dbmigration"