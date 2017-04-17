# simAS
simAS Group work for Protocol Processing course

17.4, Timo  
Almost everything now is interfaced properly. Object of class Port has *connected_to* and *belongs_to_router*. Naming convention changed to pythonish from javaish

17.4, Timo  
Reworked database.py, created wire, router, port and network modules. database.py is just collection of functions, wire, router, port and network are modules with classes in them.  
Logic of network is naturally in network.py module  
*Updated executable(main) scripts to start with Caps. At the moment ViewConfig.py and InitDb.py*

15.4, Timo  
Table Packets added to SQL, file zeija removed

2.4, Timo  
Removed database from package to module. It is not that big project.  

26.3, Timo  
All right, some bones and some meat on bones.  
initDb.py is independent python script which initializes database with information from  
fill.sql - which has two tables, Routers and Ports. !!! Please observe structure and suggest additions  
main.db - sqlite3 database, made up from fill.sql  

then, there is only one package, which has only _init_.. could be sufficient enough  
database object has database as object (da-a) and cursor object, for communicating with database  
command print for rows is bogus and obsololete, I am thinking of return format from database, and.. well.. it is yet to be considered.
