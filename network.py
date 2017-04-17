from router import Router
from port import Port
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
    def router_by_port_id(self,PortId): #returns Router object by port id, to which it belongs, bit ineffective, but will do.
        for iterate_router in self.Routers:
            for iterate_port in iterate_router.Ports:
                if (iterate_port.Id==PortId):
                    return iterate_router
        return None
    def port_by_id(self,PortId): #returns Port object bu port id
        for iterate_router in self.Routers:
            for iterate_port in iterate_router.Ports:
                if (iterate_port.Id==PortId):
                    return iterate_port
        return None
    def port_is_connected_to(self,PortId): #returns port object to which port_id is connected
        for wire in database.ListWires():
            if (wire.Port1Id==PortId):
                return self.port_by_id(Network,wire.Port2Id)
            elif (wire.Port2Id==PortId):
                return self.port_by_id(Network,wire.Port1Id)
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
            def connected_to(self): #function of Port object, returns Port object to which Port is connected
                return Network.port_is_connected_to(Network,self.Id)
            def belongs_to_router(self): #returns Router object, master of Port.               
                return Network.router_by_port_id(Network,self.Id)
                