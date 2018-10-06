import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=den1.mssql3.gear.host;DATABASE=dashtesting;UID=dashtesting;PWD=Ck0XQMB_Or4!',autocommit=True)
cursor = cnxn.cursor()


# qry = "DROP TABLE IF EXISTS dbo.LiveStatsFromSQLServer;CREATE TABLE dbo.LiveStatsFromSQLServer(ID int identity(1,1),Num TINYINT NOT NULL)"
# cursor.execute(qry)

for i in range(1000):
    qry2 = "INSERT INTO dbo.LiveStatsFromSQLServer(num) SELECT ABS(CHECKSUM(NewId())) % 14 WAITFOR DELAY '00:00:01.500'"
    cursor.execute(qry2)
