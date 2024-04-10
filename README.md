# Coding challenge
This project provides a local REST API and hosted REST APIs in Azure. This API was built with FastAPI to access and read CSV files stored in Azure Blob Storage, insert the data of those CSV files into Azure SQL tables and then compute two metrics. Also, this project provides some visualization of the table where the CSV data is inserted and the metrics.

Features:

* Retrieves data from CSV files in a specified Azure Blob Storage container.
* Exposes an endpoint to fetch data by filename.
* Returns the CSV data structure as JSON (headers and rows).
* Inserts the data into Azure SQL tables.
* Compute two metrics by using the inserted data.
* Inserts the metrics data in its corresponding Azure SQL table.

# Hosted REST API in Azure

## Step to step to deploy the API by using a local folder

First you need to have an Azure subscription, for example, a trial Azure Subscription. Then enter to the [Azure Portal](https://portal.azure.com/) and search for App Services.

![App Services](images/hosted_api/local_folder/1_app_services.jpg)

The use the Create option and select Web App.

![Create option](images/hosted_api/local_folder/2_create_option.jpg)

Next we complete the basic information fields, for example, select an existing resource group o choose to create a new one, choose a name for the app service. In this case we use the Code option to publish the API and the runtime stack. Also we select a region and a pricing plan.

![Basic information](images/hosted_api/local_folder/3_basic_fields.jpg)

Next we go to Monitoring tab and enable the application insights that will alow to see the logs.

![Monitoring option](images/hosted_api/local_folder/4_monitoring_fields.jpg)

Finally, we go to Review + Create tab, wait some seconds and click on Create option.

![Review and create](images/hosted_api/local_folder/5_review_create.jpg)

Then we wait for the app service to be deployed.

![App Service deployed](images/hosted_api/local_folder/7_app_service_deployed.jpg)

A possible issue that may appear can be that the region selected can have a quota of 0 instances. This can be solved by changing the region on the Basics tab.

![Possible issue](images/hosted_api/local_folder/6_possible_subscription_issue.jpg)

Now we open Visual Studio Code and install the Azure App Service extension. This will help us later to see app deploying. We can use this extension to create the app service.

![Azure App Service VSCode extension](images/hosted_api/local_folder/8_vscode_azure_app_service_extension.jpg)

Then we go to the Azure left panel option and select to sign in Azure.

![Sign in Azure account](images/hosted_api/local_folder/9_vscode_signin_azure_account.jpg)

After we signed in with our Azure account we will see the name of our subscription.

![Azure subscription](images/hosted_api/local_folder/10_vscode_azure_subscription.jpg)

Next on App Services is going to appear all the app services deployed. We right click on the app service deployed steps before and select Deploy to Web App.

![Deploy to Webb App option](images/hosted_api/local_folder/11_vscode_deploy_app1.jpg)

Then we browser the local folder of our coding project we want to deploy.

![Selecting local folder](images/hosted_api/local_folder/12_vscode_deploy_app2.jpg)

When this pop up window appear we choose Deploy to deploy the app on the app service we create before. 

![Pop up window](images/hosted_api/local_folder/13_vscode_deploy_app3.jpg)

Now we wait until the app is deployed.

![App deploying](images/hosted_api/local_folder/14_vscode_deploy_app4.jpg)

![App deployed](images/hosted_api/local_folder/15_vscode_deployed_app.jpg)

An additional configuration that can be made is to add a startup command. Then we go to the app service deployed in Azure and search the Configuration option.

![App service configuration](images/hosted_api/local_folder/16_app_service_configuration.jpg)

We write a startup command in case we need one and click on Save.

![Startup command](images/hosted_api/local_folder/17_app_service_startup_command.jpg)


## Step to step to deploy the API by using a GitHub Repository

We go to [Azure Portal](https://portal.azure.com/) and search for App Services.

![App Services](images/hosted_api/github_repository/1_app_services.jpg)

Then use the Create option and select Web App.

![Create option](images/hosted_api/github_repository/2_create_option.jpg)

Next we complete the basics fields that are the same as we completed before for the previous app service.

![Basic fields](images/hosted_api/github_repository/3_basic_fields.jpg)

After that we go to Deployment tab and select our GitHub account. Also, we select the repository and branch to use.

![Deployment fields](images/hosted_api/github_repository/4_deployment_fields.jpg)

Next we go to Monitoring tab and enable the application insights to activate the log stream.

![Monitoring fields](images/hosted_api/github_repository/5_monitoring_fields.jpg)

Finally, we go to Review + Create tab, wait some seconds and click on Create option.

![Review and create](images/hosted_api/github_repository/6_review_create.jpg)

And wait for the app service to be deployed.

![App service deployed](images/hosted_api/github_repository/7_app_service_deployed.jpg)

We can also add a startup command by going to Configuration.

![App service deployed](images/hosted_api/github_repository/8_app_service_configuration.jpg)

Then adding the command and click on Save.

![App service deployed](images/hosted_api/github_repository/9_app_service_startup_command.jpg)

After that we can use the web app deployed.

![Web app page](images/hosted_api/github_repository/10_app_service_fastapi.jpg)

When a GitHub repository is used to deploy the web app. On the branch we select, is going to create the following directories.

![GitHub workflow folder](images/hosted_api/github_repository/11_github_workflows_folder.jpg)

Inside the workflow subdirectory is a .yml file.

![GitHub workflow file](images/hosted_api/github_repository/12_github_workflows_file.jpg)

Everytime we made changes on this branch, is going to run a workflow to redeploy the changes on the Azure web app. We can see the workflows on the Actions tab of the repository.

![GitHub actions](images/hosted_api/github_repository/13_github_actions_workflows.jpg)


## Step to step to deploy the API by using a Docker container

Before we create the app service using a Docker container. We need a Dockerfile and then to follow some commands to build the docker image and to push that image to Docker Hub.

In this repository there is a Dockerfile from which you can guide yourself to write your own.

After creating the Dockerfile, we are going to execute the next commands on CMD console or in a CMD terminal on Visual Studio Code.

First we need to logout

```bash
docker logout
```

![Logging out docker](images/hosted_api/docker_container/1_loggingout_docker.jpg)

Then we Login to docker and write your username and password. It is the same username and password of your Docker account.

```bash
docker login
```

![Logging in docker](images/hosted_api/docker_container/2_loginin_docker.jpg)

![Logging in docker](images/hosted_api/docker_container/3_loginin_docker_password.jpg)

![Logging in docker](images/hosted_api/docker_container/4_loginin_docker_succeed.jpg)

Next go inside your project folder

```bash
cd path_project
```

We build the docker image

```bash
docker build -t image_name .
```

![Building the docker image](images/hosted_api/docker_container/5_docker_image_built.jpg)

Validate the image was built

```bash
docker images
```

![Validating](images/hosted_api/docker_container/6_docker_images.jpg)

The docker images also appear on the Docker desktop app.

![Docker images on desktop app](images/hosted_api/docker_container/7_docker_images_app.jpg)

Then tag your image created and specify a name for the target image. It is important to specify the username on this command.

```bash
docker tag name_source_image:tag username/name_target_image:tag
```

For example the command can be:

```bash
docker tag rest_api_lechu:latest lechuc/coding_challenge:latest
```

![Tagging the image](images/hosted_api/docker_container/8_tagging_docker_image.jpg)

When tagging an image, creates the new image tagged and we can also validate it on the Docker desktop app.

![Docker tagged image on app](images/hosted_api/docker_container/9_tagging_docker_image_app.jpg)

And finally push your tagged image to Docker Hub

```bash
docker push lechuc/coding_challenge:latest
```

![Pushing the image to Docker Hub](images/hosted_api/docker_container/10_pushing_image.jpg)

The docker image pushed to Docker Hub also appear on the desktop app.

![Pushed image on desktop app](images/hosted_api/docker_container/11_pushing_image_app.jpg)

And on the Docker Hub web page.

![Docker Hub repository](images/hosted_api/docker_container/12_docker_hub_repository.jpg)

Now we create the app service on Azure. Go [Azure Portal](https://portal.azure.com/) and search for App Services.

![App Services](images/hosted_api/docker_container/13_app_services.jpg)

Then use the Create option and select Web App.

![Create option](images/hosted_api/docker_container/14_create_option.jpg)

Next we complete the basics fields. In this case we choose the Container option to publish and the operating system of this container.

![Basic fields](images/hosted_api/docker_container/15_basic_fields.jpg)

Then go to Container tab, select the Docker Hub option, choose Public on Access Type, because the container is public. Write the name of the image and his tag.

![Container tab](images/hosted_api/docker_container/16_container_tab.jpg)

On the Monitoring tab, enable the application insights to activate the log stream.

![Monitoring fields](images/hosted_api/docker_container/17_monitoring_fields.jpg)

And then wait for the web app to be deployed.

![Deploying the web app](images/hosted_api/docker_container/18_deploying_app_service.jpg)

After that the web app is ready to use it.

![FastAPI web app](images/hosted_api/docker_container/19_fastapi_web_app.jpg)


## Using the hosted API linked to a GitHub repository 

This REST API was hosted using service App Services of Azure and the main branch of the GitHub repository. To test it, just use the following link and try the endpoints.

https://restapi-webapp-github.azurewebsites.net/docs

Or you can use the direct link to test the endpoints.

The following links are to read the data of the CSV files and to insert that data into the corresponding Azure SQL tables.

https://restapi-webapp-github.azurewebsites.net/csv/departments.csv

https://restapi-webapp-github.azurewebsites.net/csv/jobs.csv

https://restapi-webapp-github.azurewebsites.net/csv/hired_employees.csv

And the following link are to compute the metrics and to insert the metric data into their corresponding Azure SQL tables.

https://restapi-webapp-github.azurewebsites.net/hired_by_quarter

https://restapi-webapp-github.azurewebsites.net/most_hired_in_2021

Also there is a feature to clean the table before inserting the data of each CSV file and to clean the data of the metrics table using the following links.

https://restapi-webapp-github.azurewebsites.net/clean_table/jobs

https://restapi-webapp-github.azurewebsites.net/clean_table/departments

https://restapi-webapp-github.azurewebsites.net/clean_table/hired_employees

https://restapi-webapp-github.azurewebsites.net/clean_table/metric1

https://restapi-webapp-github.azurewebsites.net/clean_table/metric1


## Using the hosted API linked to a Docker container 

The REST API was hosted using service App Services of Azure and a Docker container published in Docker Hub. To test it, just use the following link and try the endpoints.

https://restapi-webapp-containerized.azurewebsites.net/docs

Or you can use the direct link to test the endpoints.

The following links are to read the data of the CSV files and to insert that data into the corresponding Azure SQL tables.

https://restapi-webapp-containerized.azurewebsites.net/csv/departments.csv

https://restapi-webapp-containerized.azurewebsites.net/csv/jobs.csv

https://restapi-webapp-containerized.azurewebsites.net/csv/hired_employees.csv

And the following link are to compute the metrics and to insert the metric data into their corresponding Azure SQL tables.

https://restapi-webapp-containerized.azurewebsites.net/hired_by_quarter

https://restapi-webapp-containerized.azurewebsites.net/most_hired_in_2021

Also there is a feature to clean the table before inserting the data of each CSV file and to clean the data of the metrics table using the following links.

https://restapi-webapp-containerized.azurewebsites.net/clean_table/jobs

https://restapi-webapp-containerized.azurewebsites.net/clean_table/departments

https://restapi-webapp-containerized.azurewebsites.net/clean_table/hired_employees

https://restapi-webapp-containerized.azurewebsites.net/clean_table/metric1

https://restapi-webapp-containerized.azurewebsites.net/clean_table/metric1


# Local REST API

To test the local API, please follow the next steps ahead.

Requirements:

* Python 3.11
* FastAPI
* Azure Storage SDK for Python (azure-storage-blob)
* Pyodbc
* Uvicorn
* Pandas
* SQLAlchemy

Setup:

1. Storage the input .csv input files in your Azure Blob Storage.

* Search Storage accounts on Azure Portal and enter your storage account.

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

2. Create the server in Azure SQL.

* Search Azure SQL on Azure Portal and click on Create option.

![Creating sql server](images/sql_server/1_create_option.jpg)

* Select SQL databases and Database server on Resource type to create the server.

![Deployment](images/sql_server/2_deployment_option.jpg)

* Complete the following fields of resource group, server name, location. Choose the authentication method, for example, the SQL authentication and set an adming login username and a password.

![Basics](images/sql_server/3_basics_option.jpg)

* Then continue with the next configuration (Networking, Security, etc.) or click on Review + create option to finish.

3. Create the database

* On Azure SQL, click on create again.

![Creating sql database](images/sql_database/1_create_option.jpg)
git
* Select SQL databases and Single database as Resource type and click on Create.

![Deployment](images/sql_database/2_deployment_option.jpg)

* Complete the basic fields.

![Basics](images/sql_database/3_basics.jpg)

* Then continue with the next configurations or click on Review + create to finish.

4. Install required libraries in your virtual environment:

    pip install fastapi azure-storage-blob uvicorn pyodbc pandas sqlalchemy

5. Replace placeholders in main.py:

* YOUR_AZURE_SQL_DATABASE_CONNECTION_STRING_FOR_PYODBC: Your Azure SQL Database connection string  to use with the pyodbc library.
* YOUR_AZURE_SQL_DATABASE_CONNECTION_STRING_FOR_SQLALCHEMY: Your Azure SQL Database connection string to use with the sqlalchemy library.
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

3. Test retrieving specific CSV data by replacing {filename} with the actual file name in the URL (e.g., http://localhost:8000/csv/jobs.csv).

* In the following images, we can see the results of the endpoints. We can find these screenshots on the images folder.

* First, the input CSV files uploaded in the storage account.

![CSVs uploaded in storage account](images/endpoints/csv_inserted_data/input_csvs_in_storage.PNG)

* Then we see the results on Fast API after the CSV data is inserted on the corresponding Azure SQL table.

![Jobs data inserted](images/endpoints/csv_inserted_data/jobs_csv_inserted.PNG)

![Departments data inserted](images/endpoints/csv_inserted_data/departments_csv_inserted.PNG)

![Hired Employees data inserted](images/endpoints/csv_inserted_data/hired_employees_csv_inserted.PNG)

* And the data on the Azure SQL tables

![Jobs table](images/endpoints/csv_inserted_data/jobs_azure_sql_table.PNG)

![Number of rows in Jobs table](images/endpoints/csv_inserted_data/count_jobs_azure_sql_table.PNG)

![Departments table](images/endpoints/csv_inserted_data/departments_azure_sql_table.PNG)

![Number of rows in Departments table](images/endpoints/csv_inserted_data/count_departments_azure_sql_table.PNG)


![Hired Employees table](images/endpoints/csv_inserted_data/hired_employees_azure_sql_table.PNG)

![Number of rows in Hired Employees table](images/endpoints/csv_inserted_data/count_hired_employees_azure_sql_table.PNG)

* Here we can see the result on Fast API of the first metric computed about the number of employees hired for each job and department for each quarter in 2021.

![1 - First metric results](images/endpoints/first_metric/first_metric_1.PNG)

![2 - First metric results](images/endpoints/first_metric/first_metric_2.PNG)

* And also for the second metric of the departments that hired more employees than the mean of employees hired in 2021 of all departments.

![1 - Second metric results](images/endpoints/second_metric/second_metric_1.PNG)

![2 - Second metric results](images/endpoints/second_metric/second_metric_2.PNG)

* That data obtained of both metrics were also inserted in Azure SQL tables. In the next pics, appears some data of the first metric.

![Firt metric table](images/endpoints/first_metric/first_metric_azure_sql_table.PNG)

![Number of rows in first metric table](images/endpoints/first_metric/count_first_metric_azure_sql_table.PNG)

* And also for the second metric.

![Second metric table](images/endpoints/second_metric/second_metric_azure_sql_table.PNG)

![Number of rows in second metric table](images/endpoints/second_metric/count_second_metric_azure_sql_table.PNG)

# Testing

To execute the automated tests use the following command.

```python
pytest -r tests
```

![All tests passed](images/tests/1_all_tests.jpg)

If you want to execute an specified test use the command

```python
pytest -r tests/test_api_endpoints.py::test_get_csv_data
```

![Specified test](images/tests/2_specified_test.jpg)

# Visualization

For this part we used Power BI Desktop that can be downloaded [here](https://www.microsoft.com/en-us/download/details.aspx?id=58494).

Then we connected Power BI to the Azure SQL to retrieve the data of each table (jobs, departments, hired_employees, metric1 and metric2). After we added some charts using the data imported and published the dashboard on a Power BI workspace. Also, we published to the web, so it can be accessed with the following link.

https://app.powerbi.com/view?r=eyJrIjoiYjBiM2JjNzAtOTc2Yy00ZTdkLTllYTctY2RlMThkM2RjYmU1IiwidCI6ImI5OWQyYzkwLWZhYzYtNDlhZi05NTVhLTVhY2FiZDFhOGEyMCIsImMiOjR9&pageName=ReportSection