# SQLSERVER PYODBC Module 

## Installation for linux guys

1. Install a driver for your linux machine!
2. I recommend `FreeTDS` 

### Installing `FreeTDS`

1. Install pre-requisite packages
```
sudo apt-get install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc
```

2. Point `odbcinst.ini` to the driver in `/etc/odbcinst.ini`
```
[FreeTDS]
Description = v0.91 with protocol v7.2
Driver = MYDRIVERPATH
```

where `MYDRIVERPATH` is the path of the `libtdsodbc.so` file

Hint! Look in the `/usr/lib/mylinuxdistro/odbc`  folder!
Will implement script in the future to install/automate this for linux solutions.

````
pip install sqlserver
````

## Installation for windows guys
````
pip install sqlserver
````

#### Example of ConnectionString
````
DRIVERS = db.ReturnDrivers()
# output of drivers
['SQL Server', 'ODBC Driver 17 for SQL Server', 'SQL Server Native Client 11.0', 'SQL Server Native Client RDA 11.0', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)']

# We can use a SQL ODBC Driver or FreeTDS
DRIVER={ODBC Driver 17 for SQL Server};SERVER=SERVERNAME,PORT;DATABASE=DB;UID=USERNAME;PWD=PASSWORD
````


## Usage

### Initialization
````
import sqlserver
db = sqlserver.adgsqlserver('yourconnectionstring')
````
### Commands

#### Execute Query
`parms`: ExecuteQuery(query:str)

This enables you to execute any query without any `stdout` but returns a `bool` `True` or `False` if query passes and logs `exception` in terminal as `stdout`.
```
query = 'somequery'
db.ExecuteQuery()
```

#### Return Query as Dictionary

`parms`: GetRecordsAsDict(query:str)

We use this for `select` statements or any other query that returns a `table` as a result.
```
query = "SELECT 'Connection Passed' AS Result"
db.GetRecordsAsDict(query)
```

`stdout`
```
{'results': [{'Result': 'Connection Passed'}]}
```

#### Return Query as Column List
`parms`: GetRecordsOfColumn(query:str,ColumnName:str)


We use this for `select` statements or any other query that returns a `table` as a result.
```
db.GetRecordsOfColumn("SELECT 'Connection Passed' AS Result", "Result")
```

`stdout`
```
['Connection Passed']
```

#### Create CSV Table Schema
`parms`: CreateCSVTable(csvfile:str)

Creates a SQL Table with varchar(max) columns such that it can be ready to be inserted to based on the .csv column names

Assumption: `somefile.csv`
```
name,surname,phonenumber
test,testor,01234567810
```

```
path = 'C:/somefile.csv'
db.CreateCSVTable(path)
```

In SQL Table `somefile.dbo`
```
|name|surname|phonenumber|
```

#### Insert CSV Table
`parms`: InsertCSVTable(csvfile:str)

Assumption: `somefile.csv`
```
name,surname,phonenumber
test,testor,01234567810
```
```
path = 'C:/somefile.csv'
db.InsertCSVTable(path)
```
In SQL Table `somefile.dbo`
```
--------------------------
|name|surname|phonenumber|
|----|-------|-----------|
|test|testor |01234567810|
--------------------------
```

#### Insert XML
`parms`: InsertXMLSQLTable(xmlfilepath:str)

```
xmlfilepath = 'C:/somexml.xml'
db.InsertXMLSQLTable(xmlfilepath)
```

###### Copyright ADGSTUDIOS 2022
