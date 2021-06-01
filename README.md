# pythonsqlserverclass
class to connect to SQL SERVER DB - Run queries and extract records

# usage
```
pip install sqlserver
```

# code implementation
```
import sqlserver as ss 
                 (ip,portnumber,databasename,username,password)
db = ss.sqlserver('localhost','1433','CVs','','')

                     (query                   ,columnname)
db.GetRecordsOfColumn('select * from tblUsers','personid')
```
