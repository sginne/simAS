from router import Router
from port import Port
from wire import Wire
import database

class Network(object):
    Routers=[] #Network object is going to be instantiated and contain routers in Routers[] list of objects
    def __init__(self): #Using ListRouters function from database.py we initialize Routers[] list with routers from db
        for RouterObject in database.ListRouters():
            self.Routers.append(self.Router(RouterObject.Id,RouterObject.Name))
    class Wire(Wire):
        def connected(PortId): #no self, not going to make object
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
                    
    class Router(Router): #Network.Router inherits Router from router.py and adds constructor __init__
        Ports=[] #Again, ports do not belong to network per se, they belong to router       
        def __init__(self,Id,Name):
            self.Id=Id
            self.Name=Name
            self.Ports=[]
            for PortObject in database.ListPorts():
                #print(PortObject.RouterId,self.Name)
                if (PortObject.RouterId==self.Id):
                    #self.Ports.append('a')                   
                    self.Ports.append(self.Port(PortObject.Id,PortObject.RouterId,PortObject.Ip))
                    
        class Port(Port): #Network.Router.Prt inherits Port from port.py and adds constructor __init__
            def __init__(self,Id,RouterId,Ip):
                self.Id=Id
                self.RouterId=RouterId
                self.Ip=Ip
            def belongsto(self,PortId): #Returns Router.Id of Port
                for PortObject in database.ListPorts(): #not elegant, but works
                    if (PortObject.Id==PortId):
                        return PortObject.RouterId
                return None
            def portsip(self,PortId):
                for PortObject in database.ListPorts():
                    if (PortObject.Id==PortId):
                        return PortObject.Ip
                return None
                    
                
                
                