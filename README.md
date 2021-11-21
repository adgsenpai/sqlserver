<h1> SQLSERVER PYODBC Module </h1>

##### Installation for linux guys

````
%%sh
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17
pip install sqlserver
````


##### Installation for windows guys
````
pip install sqlserver
````

#### Example of ConnectionString linux guys
````
DRIVER={ODBC Driver 17 for SQL Server};SERVER=SERVERNAME,PORT;DATABASE=DB;UID=USERNAME;PWD=PASSWORD
````


##### Usage
````
import sqlserver
db = sqlserver.adgsqlserver('yourconnectionstring')

db.(whateverfunctions in the modules)
returns data
````

###### Copyright ADGSTUDIOS 2021
