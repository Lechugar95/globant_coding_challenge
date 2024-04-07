# Base image with desired Python version (adjust as needed)
FROM python:3.11.4

# Update package lists and install unixodbc
RUN apt-get update && apt-get install -y unixodbc
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set working directory within the container
WORKDIR /globant_coding_challenge

# Copy requirements file
COPY requirements.txt ./

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose the port your API listens on (adjust as needed)
EXPOSE 8000

# Command to run your application (replace with your actual command)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
