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
            connected_port=network.port_is_connected_to(port.Id)
            if connected_port:
                print ("----Is connected to P{}, with IP={} which belongs to R{}.Name='{}'".format(connected_port.Id,connected_port.Ip,network.router_by_port_id(connected_port.Id).Id,network.router_by_port_id(connected_port.Id).Name))