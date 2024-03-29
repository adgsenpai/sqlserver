# SQLSERVER PYODBC Module 

### Academic Papers Regarding this Module

- [The Mass Insertion of SQL Server Records Algorithm](https://zenodo.org/record/7306173#.Y29OmnZBxD9)

## Installation for linux guys

1. Install a driver for your linux machine!
2. I recommend `FreeTDS` 

### Installing `FreeTDS` from bash script
You may look at my script @ https://github.com/adgsenpai/InstallFreeTDS

### Installing `FreeTDS` Manually

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

#### Generate Insert Script
`parms`: InsertScript(df:DataFrame,tblName:str,isNEWID:bool=False)

```
df = pd.DataFrame({'name':['test','test2'],'surname':['testor','testor2'],'phonenumber':['01234567810','01234567810']})
db.InsertScript(df,'somefile')
```

`stdout`
```
'''
INSERT INTO [somefile]
VALUES
('test','testor','01234567810'),
('test2','testor2','01234567810')
'''
```

#### Generate Update Script
`parms`: UpdateScript(dataDict:dict,whereCondition:str,tblName:str)

```
dataDict = {'name':'test','surname':'testor','phonenumber':'01234567810'}
whereCondition = "name = 'test'"
db.UpdateScript(dataDict,whereCondition,'somefile')
```

`stdout`
```
'''
UPDATE [dbo].[somefile]
SET
[name] = 'test',
[surname] = 'testor',
[phonenumber] = '01234567810'
WHERE
name = 'test'
'''
```

#### Generate Delete Script
`parms`: DeleteScript(whereCondition:str,tblName:str)

```
whereCondition = "name = 'test'"
db.DeleteScript(whereCondition,'somefile')
```

`stdout`
```
'''
DELETE FROM [dbo].[somefile]
WHERE
name = 'test'
'''
```

#### Generate Select Script
`parms`: SelectScript(whereCondition:str,tblName:str)

```
whereCondition = "name = 'test'"
db.SelectScript(whereCondition,'somefile')
```

`stdout`
```
'''
SELECT * FROM [dbo].[somefile]
WHERE
name = 'test'
'''
```

#### Execute Script
`parms`: ExecuteScript(query:str)

```
query = "SELECT 'Connection Passed' AS Result"
db.ExecuteScript(query)
```

`stdout`
```
{'results': [{'Result': 'Connection Passed'}]}
```

###### Copyright ADGSTUDIOS 2023
