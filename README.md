# Coding challenge
This project provides a local REST API built with FastAPI to access and read CSV files stored in Azure Blob Storage.

Features:

Retrieves data from CSV files in a specified Azure Blob Storage container.
Exposes an endpoint to fetch data by filename.
Returns the CSV data structure as JSON (headers and rows).
Requirements:

* Python 3.6 or later
* FastAPI
* Azure Storage SDK for Python (azure-storage-blob)
* Pydantic

Setup:

1. Install required libraries:

    pip install fastapi azure-storage-blob pydantic uvicorn pyodbc

2. Replace placeholders in main.py:

* YOUR_AZURE_STORAGE_CONNECTION_STRING: Your Azure Storage connection string.
* YOUR_CONTAINER_NAME: The name of the container containing your CSV files.

Running the API:

1. Save the script as main.py.

2. Run the script from the command line:

    python csv_api.py

This starts the FastAPI server on port 8000 by default.

Testing the API:

1. Open the FastAPI documentation in your browser:

    http://localhost:8000/docs

2. Explore the available endpoint (/csv/{filename}) and its usage.

3. Test retrieving specific CSV data by replacing {filename} with the actual file name in the URL (e.g., http://localhost:8000/csv/data.csv).