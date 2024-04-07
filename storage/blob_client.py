from azure.storage.blob import BlobServiceClient
from config import storage_connection_string, container_name

def get_blob_client():
    """Creates a BlobServiceClient for interacting with Azure Blob Storage."""

    # Create BlobServiceClient and get the container client
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)

    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)
    
    return container_client