# ADGSTUDIOS 2022
import pyodbc
import pandas as pd
from pathlib import Path
import pathlib

class adgsqlserver():
    def __init__(self, connectionstring):
        self.connectionstring = connectionstring
        
    def fields(self, cur):
        results = {}
        column = 0
        for d in cur.description:
            results[d[0]] = column
            column = column + 1
        return results

    def ReturnDrivers(self):
        return pyodbc.drivers()

    def GetRecordsOfColumn(self, SelectQuery, ColumnName):
        try:
            conn = pyodbc.connect(self.connectionstring)
            cursor = conn.cursor()
            cursor.execute(SelectQuery)
            field_map = self.fields(cursor)
            values = []
            for row in cursor:
                values.append(row[field_map[ColumnName]])
            return values
        except Exception as e:
            print(e)
            return False

    def ExecuteQuery(self, Query):
        try:
            conn = pyodbc.connect(self.connectionstring)
            cursor = conn.cursor()
            cursor.execute(Query)
            cursor.commit()
            return True
        except Exception as e:
            print(e)
            return False
            

    def GetRecordsAsDict(self, SelectQuery):
        try:
            conn = pyodbc.connect(self.connectionstring)
            cursor = conn.cursor()
            cursor.execute(SelectQuery)
            return {'results':
                    [dict(zip([column[0] for column in cursor.description], row))
                     for row in cursor.fetchall()]}
        except Exception as e:
            print(e)
            return False

    def CreateCSVTable(self,csvfile):
            df = pd.read_csv(csvfile)
            tablename = pathlib.Path(csvfile).stem
            payload = ''
            columns = list(df.keys())
            for i,column in enumerate(columns):
                if i == len(columns)-1:
                  payload += ('['+column+']'+' varchar(max)'+'\n')
                else:
                  payload += ('['+column+']'+' varchar(max)'+','+'\n')
                    
            query = f'''
            IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{tablename}' AND TABLE_SCHEMA = 'dbo')
            BEGIN
                DROP TABLE [dbo].[{tablename}]
                CREATE TABLE [dbo].[{tablename}]
                (
                    {payload}
                );
            END
            ELSE
                CREATE TABLE [dbo].[{tablename}]
                (
                    {payload}
                );
            '''
            try:
                conn = pyodbc.connect(self.connectionstring)
                cursor = conn.cursor()
                cursor.execute(query)
                cursor.commit()
                return 'Table Created'
            except Exception as e:
                print(e)
                return False
        
    def InsertCSVData(self,csvfile):
        df = pd.read_csv(csvfile)
        tablename = pathlib.Path(csvfile).stem
        columns = list(df.keys())
        payload = ''
        for index, row in df.iterrows():
            record = '('
            for i,column in enumerate(columns):
                record += "'"+str(row[column]).replace("'"," ")+"'" + ','
            record = record[:-1]
            payload += record+'),'+'\n'

            if index % 1000 == 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connectionstring)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)
                 
                payload = ''

        if len(payload) > 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connectionstring)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)

    def InsertXMLSQLTable(self,path):
            df = pd.read_xml(path)
            datapath = Path(path)
            df.to_csv(datapath.name+'.csv')
            self.CreateCSVTable(datapath.name+'.csv')
            self.InsertCSVData(datapath.name+'.csv')


    def CreateTableScript(self,df,tblName):
        # create the table creation script
        # df = dataframe
        # tblName = table name
        # returns a string
        columns = list(df.keys())
        payload = ''
        for i,column in enumerate(columns):
            payload += '['+column+']'+' '+'VARCHAR(max)' + ','
        payload = payload[:-1]
        query = f'''
        IF OBJECT_ID('dbo.{tblName}', 'U') IS NOT NULL
        BEGIN
            DROP TABLE [dbo].[{tblName}]
        END
        CREATE TABLE [dbo].[{tblName}]
        (
            {payload}
        );
        '''
        return query

    def InsertScript(self,df,tblName,isNEWID=False):
        # create the insert/update script
        # df = dataframe
        # tblName = table name
        # isNEWID = if true, then the ID column will be a NEWID()
        # returns a string
        columns = list(df.keys())
        payload = ''
        for index, row in df.iterrows():
            record = '('
            for i,column in enumerate(columns):
                if isNEWID and column == 'ID':
                    record += 'NEWID()' + ','
                else:
                    record += "'"+str(row[column]).replace("'"," ")+"'" + ','
            record = record[:-1]
            payload += record+'),'+'\n'

            if index % 1000 == 0:
                query = f'''
                INSERT INTO [{tblName}]
                VALUES
                {payload[:-2]}
                '''
                payload = ''

        if len(payload) > 0:
                query = f'''
                INSERT INTO [{tblName}]
                VALUES
                {payload[:-2]}
                '''
        return query

    def UpdateScript(self,dataDict,whereCondition,tblName):
        # create the update script
        # dataDict = dictionary of column name and value
        # whereCondition = where condition
        # returns a string
        payload = ''
        for key in dataDict.keys():
            payload += '['+key+']'+' = '+"'"+str(dataDict[key]).replace("'"," ")+"'" + ','
        payload = payload[:-1]
        query = f'''
        UPDATE [dbo].[{tblName}]
        SET
        {payload}
        WHERE
        {whereCondition}
        '''
        return query 

    def DeleteScript(self,whereCondition,tblName):
        # create the delete script
        # whereCondition = where condition
        # returns a string
        query = f'''
        DELETE FROM [dbo].[{tblName}]
        WHERE
        {whereCondition}
        '''
        return query

    def SelectScript(self,whereCondition,tblName):
        # create the select script
        # whereCondition = where condition
        # returns a string
        query = f'''
        SELECT * FROM [dbo].[{tblName}]
        WHERE
        {whereCondition}
        '''
        return query
