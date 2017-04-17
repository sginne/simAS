from router import Router
from port import Port
from wire import Wire
import database

class Network(object):
    Routers=[] #Network object is going to be instantiated and contain routers in Routers[] list of objects
    def __init__(self): #Using ListRouters function from database.py we initialize Routers[] list with routers from db
        for RouterObject in database.ListRouters():
            self.Routers.append(self.Router(RouterObject.Id,RouterObject.Name))
    def router_by_id(self,Id): #return Router object from Network.Routers[] by id or None if none
        for iterate_router in self.Routers:
            if (iterate_router.Id==Id):
                return iterate_router
        return None
    def router_by_port_id(self,PortId):
        for iterate_router in self.Routers:
            for iterate_port in iterate_router.Ports:
                if (iterate_port.Id==PortId):
                    return iterate_router
        return None
    def port_by_id(self,PortId):
        for iterate_router in self.Routers:
            for iterate_port in iterate_router.Ports:
                if (iterate_port.Id==PortId):
                    return iterate_port
        return None
    def port_is_connected_to(self,PortId):
        for wire in database.ListWires():
            if (wire.Port1Id==PortId):
                return self.port_by_id(wire.Port2Id)
            elif (wire.Port2Id==PortId):
                return self.port_by_id(wire.Port1Id)
        return None

                    
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
                    
                
                
                