'''
Created on Mar 26, 2017

@author: sginne
'''
import database

if __name__ == '__main__':
    DbObject=database
    network=database.Network() #network initialisation
    for i in network.Routers: #after network initialized, we have list of Routers, iterating 
        print ("There is router {}, name is {}. Ports:".format(i.Id,i.Name))
        for j in i.Ports: #network.Routers[x].Ports has Port in Ports[x] list
            print("--PortId={}, which belongs to {} and has IP={}".format(j.Id,j.RouterId,j.Ip))