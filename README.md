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

1. Storage the input .csv input files in your Azure Blob Storage.

* Go to your storage account in Azure Portal.
![Storage account](images/csv_upload/1_storage_account.jpg)

* Then go to Storage browser menu.
![Storage browser](images/csv_upload/2_storage_browser.jpg)

* Click on Blob container menu.
![Blob container](images/csv_upload/3_blob_container.jpg)

* Go to Add container option.
![Adding container](images/csv_upload/4_add_container.jpg)

* Open your container and click on Add directory option.
![Adding virtual directory](images/csv_upload/5_add_directory.jpg)

* Go into your directory, click on Upload option to upload the .csv files.
![Uploading files](images/csv_upload/6_upload_files.jpg)

1. Install required libraries:

    pip install fastapi azure-storage-blob pydantic uvicorn pyodbc

2. Replace placeholders in main.py:

* YOUR_AZURE_STORAGE_CONNECTION_STRING: Your Azure Storage connection string.
* YOUR_CONTAINER_NAME: The name of the container containing your CSV files.

Running the API:

1. Save the script as main.py.

2. Run the script from the command line:

    python main.py

This starts the FastAPI server on port 8000 by default.

Testing the API:

1. Open the FastAPI documentation in your browser:

    http://localhost:8000/docs

2. Explore the available endpoint (/csv/{filename}) and its usage.

3. Test retrieving specific CSV data by replacing {filename} with the actual file name in the URL (e.g., http://localhost:8000/csv/data.csv).
