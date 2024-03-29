from fastapi import FastAPI, Query
from azure.storage.blob import BlobServiceClient
from pydantic import BaseModel

# Replace with your connection string
connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"

# Container name where your CSV files are stored
container_name = "YOUR_CONTAINER_NAME"

app = FastAPI()

class CSVData(BaseModel):
    headers: list[str]
    data: list[list[str]]

@app.get("/csv/{filename}")
async def get_csv_data(filename: str):
    try:
        # Create BlobServiceClient with the connection string
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Get a reference to the container
        container_client = blob_service_client.get_container_client(container_name)
        
        # Download the specific CSV blob
        blob_client = container_client.get_blob_client(filename)
        download_stream = blob_client.download_blob()  # No need to await here
        
        # Read the CSV data from the download stream
        csv_data = download_stream.content_as_text(encoding="utf-8").splitlines()
        headers = csv_data[0].split(",")
        data = [row.split(",") for row in csv_data[1:]]
        
        return CSVData(headers=headers, data=data)
    except Exception as e:
        # Handle errors appropriately (e.g., return HTTP status code 404)
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)