'''
Created on Apr 2, 2017

@author: sginne
'''
import sqlite3
DbConnection = None
DbCursor= None

class Network(object):
    Routers=[]
    def __init__(self):
        for RouterObject in ListRouters():
            self.Routers.append(self.Router(RouterObject.Id,RouterObject.Name))
                    
    class Router(object):
        Id=0
        Name='x'
        Ports=[]
        def __init__(self,Id,Name):
            self.Id=Id
            self.Name=Name
            self.Ports=[]
            for PortObject in ListPorts():
                #print(PortObject.RouterId,self.Name)
                if (PortObject.RouterId==self.Id):
                    #self.Ports.append('a')                   
                    self.Ports.append(self.Port(PortObject.Id,PortObject.RouterId,PortObject.Ip))
        class Port(object):
            Id=0
            RouterId=0
            Ip='x.x.x.x'
            def __init__(self,Id,RouterId,Ip):
                self.Id=Id
                self.RouterId=RouterId
                self.Ip=Ip
            

class Router(object):
    Id=0
    Name='X'
class Port(object):
    Id=0
    RouterId=0
    Ip='x.x.x.x'
class Wire(object):
    Id=0
    Port1Id=0
    Port2Id=0
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
def ListPorts(Where=''):
    out=[]
    DbConnection = sqlite3.connect('main.db')
    DbCursor=DbConnection.cursor()
    #cursor=DbCursor.execute("SELECT * FROM PORTS "+Where)
    for row in DbCursor.execute("SELECT * FROM PORTS "+Where).fetchall():
        Obj=Router()
        Obj.Id=row[0]
        Obj.RouterId=row[1]
        Obj.Ip=row[2]
        out.append(Obj)
    DbConnection.close()
    return out
    
    
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