'''
Created on Mar 26, 2017

@author: sginne
'''
import database

if __name__ == '__main__':
    DbObject=database
    network=database.Network() #network initialisation
    for router in network.Routers: #after network initialized, we have list of Routers, iterating 
        print ("There is router {}, name is {}. Ports:".format(router.Id,router.Name))
        for port in router.Ports: #network.Routers[x].Ports has Port in Ports[x] list
            print("--PortId={}, which belongs to {} and has IP={}".format(port.Id,port.RouterId,port.Ip))
            for wire in database.ListWires():
                if (port.Id==wire.Port1Id):
                    print ("----Port is connected to another port with ID={}".format(wire.Port2Id))
                elif (port.Id==wire.Port2Id):
                    print ("----Port is connected to another port with ID={}".format(wire.Port1Id))
