'''
Created on Apr 2, 2017

@author: sginne
'''
import sqlite3
from router import Router
from port import Port
from wire import Wire
DbConnection = None
DbCursor= None


    
#database initialization and sql command execution.
def InitSQL(FileName): 
    DbConnection = sqlite3.connect('main.db')
    DbCursor=DbConnection.cursor()
    DatabaseFile=open(FileName,'r')
    SqlFile=DatabaseFile.read()
    DatabaseFile.close()
    SqlCommands = SqlFile.split(';')
    for command in SqlCommands:
        DbCursor.execute(command)
    DbConnection.commit()
    DbConnection.close()
    
# Loading all ports available for each router.
def ListPorts(Where=''):
    out=[]
    DbConnection = sqlite3.connect('main.db')
    DbCursor=DbConnection.cursor()
    #cursor=DbCursor.execute("SELECT * FROM PORTS "+Where)
    for row in DbCursor.execute("SELECT * FROM PORTS "+Where).fetchall():
        Obj=Port()
        Obj.Id=row[0]
        Obj.RouterId=row[1]
        Obj.Ip=row[2]
        out.append(Obj)
    DbConnection.close()
    return out
    
# Load the list of routers conneted from database.    
def ListRouters(Where=''):
    out=[]
    DbConnection = sqlite3.connect('main.db')
    DbCursor=DbConnection.cursor()
    for row in DbCursor.execute("SELECT * FROM ROUTERS "+Where).fetchall():
        Obj=Router()
        Obj.Id=row[0]
        Obj.Name=row[1]
        out.append(Obj)
    DbConnection.close()
    return out
def ListWires(Where=''):
    out=[]
    DbConnection = sqlite3.connect('main.db')
    DbCursor=DbConnection.cursor()
    for row in DbCursor.execute("SELECT * FROM WIRES "+Where).fetchall():
        Obj=Wire()
        Obj.Id=row[0]
        Obj.Port1Id=row[1]
        Obj.Port2Id=row[2]
        out.append(Obj)
    DbConnection.close()
    return out
