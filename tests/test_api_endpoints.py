import os, sys
import pytest
from fastapi.testclient import TestClient
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

@pytest.fixture
def client():
    """Creates a FastAPI test client for making requests to the API."""
    with TestClient(app) as c:
        yield c

@pytest.mark.parametrize("filename", ["departments.csv","jobs.csv","hired_employees.csv"])
#@pytest.mark.parametrize("filename", ["departments.csv"])
def test_get_csv_data(client, filename):
    """Tests the /csv/{filename} endpoint to retrieve CSV data and insert it into SQL."""
    # Replace with a valid filename in your container
    #filename = "departments.csv"
    response = client.get(f"/csv/{filename}")
    assert response.status_code == 200  # Expect success status code
    assert "message" in response.json()  # Check for success message
    message = (response.json()["message"])
    print(f"Success message: {message}")
    

def test_calculate_first_metric(client):
    """Tests the /hired_by_quarter endpoint for calculating the first metric."""
    response = client.get("/hired_by_quarter")
    assert response.status_code == 200  # Expect success status code
    assert "data" in response.json()[0] # Check for data in response
    assert "message" in response.json()[1]  # Check for success message (optional)
    #message = (response.json()["message"])
    #print(f"Success message: {message}")


def test_calculate_second_metric(client):
    """Tests the /most_hired_in_2021 endpoint for calculating the second metric."""
    response = client.get("/most_hired_in_2021")
    assert response.status_code == 200  # Expect success status code
    assert "data" in response.json()[0] # Check for data in response
    assert "message" in response.json()[1]  # Check for success message (optional)
    #message = (response.json()["message"])
    #print(f"Success message: {message}")


@pytest.mark.parametrize("table_name", ["departments","jobs","hired_employees","metric1","metric2"])
#@pytest.mark.parametrize("table_name", ["departments"])
def test_truncate_table(client, table_name):
    """Tests the /truncate_table endpoint for truncating a table."""
    # Replace with an actual table name
    #table_name = "departments"
    response = client.get(f"/truncate_table?table_name={table_name}")
    assert response.status_code == 200  # Expect success status code
    assert "message" in response.json()  # Check for success message
    message = (response.json()["message"])
    print(f"Success message: {message}")
