'''
Created on Apr 2, 2017

@author: sginne
'''
import sqlite3
DbConnection = sqlite3.connect('main.db')
DbCursor=DbConnection.cursor()

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

def InitSQL(FileName):
    DatabaseFile=open(FileName,'r')
    SqlFile=DatabaseFile.read()
    DatabaseFile.close()
    SqlCommands = SqlFile.split(';')
    for command in SqlCommands:
        DbCursor.execute(command)
    DbConnection.commit()
def ListPorts(Where=''):
    out=[]
    cursor=DbCursor.execute("SELECT * FROM PORTS "+Where)
    for row in DbCursor.execute("SELECT * FROM PORTS "+Where).fetchall():
        Obj=Router()
        Obj.Id=row[0]
        Obj.RouterId=row[1]
        Obj.Ip=row[2]
        out.append(Obj)
    return out
    
    
def ListRouters(Where=''):
    out=[]
    for row in DbCursor.execute("SELECT * FROM ROUTERS "+Where).fetchall():
        Obj=Router()
        Obj.Id=row[0]
        Obj.Name=row[1]
        out.append(Obj)
    return out
    
    