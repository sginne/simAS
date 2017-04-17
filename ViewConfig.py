'''
Created on Mar 26, 2017

@author: sginne
'''
import database
from network import Network

if __name__ == '__main__': #actually IDE added it. not really necessary
    DbObject=database #module(but not class) to work with database. Included into database.py
    network=Network() #network initialisation
    for router in network.Routers: #after network initialized, we have list of Routers, iterating 
        print ("There is router {}, name is {}. Ports:".format(router.Id,router.Name))
        for port in router.Ports: #network.Routers[x].Ports has Port in Ports[x] list
            print("--PortId={}, which belongs to {} and has IP={}".format(port.Id,port.RouterId,port.Ip))
            if Network.Wire.connected(port.Id): #Network.Wire.connected takes port id as argument, returns None if itsnt connected, or portid it leads to
                print ("----PortId={} is connected to PortId={}".format(port.Id,Network.Wire.connected(port.Id)))