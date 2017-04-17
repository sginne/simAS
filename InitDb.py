'''
Created on Mar 26, 2017

@author: sginne
'''
import database

if __name__ == '__main__':
    dbObject=database
    dbObject.InitSQL('fill.sql') #reinitialize database

    