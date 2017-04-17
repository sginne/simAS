'''
Created on Mar 26, 2017

@author: sginne
'''
from network import Network

if __name__ == '__main__': #actually IDE added it. not really necessary
    network=Network() #network initialisation
    
    for router in network.Routers: #after network initialized, we have list of Routers, iterating 
        print ("There is router R{}, name is '{}'. Ports:".format(router.Id,router.Name))
        for port in router.Ports: #network.Routers[x].Ports has Port in Ports[x] list
            print("--P{}, which belongs to R{} and has IP={}".format(port.Id,port.RouterId,port.Ip))
            #connected_port=network.port_is_connected_to(port.Id)
            if port.connected_to():
                print ("----Is connected to P{}, with IP={} which belongs to R{}.Name='{}'".format(port.connected_to().Id,port.connected_to().Ip,port.connected_to().belongs_to_router().Id,port.connected_to().belongs_to_router().Name))