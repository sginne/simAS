from router import Router
from port import Port
from wire import Wire
import database

class Network(object):
    Routers=[]
    def __init__(self):
        for RouterObject in database.ListRouters():
            self.Routers.append(self.Router(RouterObject.Id,RouterObject.Name))
    class Wire(Wire):
        def connected(PortId):
            ConnectedId=PortId
            ReturnId=None
            for wire in database.ListWires():
                if (PortId==wire.Port1Id):
                    ConnectedId=wire.Port2Id
                elif (PortId==wire.Port2Id):
                    ConnectedId=wire.Port1Id
            if (ConnectedId!=PortId):
                ReturnId=ConnectedId
            return ReturnId
                    
    class Router(Router):
        Ports=[]
        def __init__(self,Id,Name):
            self.Id=Id
            self.Name=Name
            self.Ports=[]
            for PortObject in database.ListPorts():
                #print(PortObject.RouterId,self.Name)
                if (PortObject.RouterId==self.Id):
                    #self.Ports.append('a')                   
                    self.Ports.append(self.Port(PortObject.Id,PortObject.RouterId,PortObject.Ip))
        class Port(Port):
            def __init__(self,Id,RouterId,Ip):
                self.Id=Id
                self.RouterId=RouterId
                self.Ip=Ip