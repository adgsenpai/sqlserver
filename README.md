# pythonsqlserverclass
class to connect to SQL SERVER DB - Run queries and extract records

# usage
```
pip install sqlserver
```

# code implementation
```
import sqlserver as ss 
   
db = ss.sqlserver('yourconnectionstringhere')

(query,columnname)                     
db.GetRecordsOfColumn('select * from tblUsers','personid')
```
