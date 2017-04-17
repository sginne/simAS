DROP TABLE IF EXISTS Routers;
DROP TABLE IF EXISTS Ports;
DROP TABLE IF EXISTS Packages;
DROP TABLE IF EXISTS Wires;
CREATE TABLE `Routers` (
	`Id`	INTEGER NOT NULL UNIQUE,
	`Name`	TEXT UNIQUE,
	PRIMARY KEY(Id)
);
INSERT INTO `Routers` (Id,Name) VALUES (1,'First');
INSERT INTO `Routers` (Id,Name) VALUES (2,'Second');
INSERT INTO `Routers` (Id,Name) VALUES (3,'Third');
CREATE TABLE `Ports` (
	`Id`	INTEGER NOT NULL UNIQUE,
	`Router_Id`	INTEGER,
	`Ip`	TEXT,
	PRIMARY KEY(Id)
);
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (1,1,'192.168.0.1');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (2,1,'192.168.0.2');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (3,1,'192.168.0.3');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (4,2,'192.168.0.4');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (5,2,'192.168.0.5');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (6,3,'192.168.0.6');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (7,3,'192.168.0.7');
CREATE TABLE `Packages` (
   `Id`	INTEGER NOT NULL UNIQUE,
	`Position` TEXT,
	`Version` INTEGER,
	`IHL` INTEGER,
	`DSCP` INTEGER,
	`ECN` INTEGER,
	`Length` INTEGER,
	`Identification` INTEGER,
	`Flags` INTEGER,
	`Offset` INTEGER,
	`TTL` INTEGER,
	`Protocol` INTEGER,
	`Checksum` INTEGER,
	`Source` INTEGER,
	`Destination` INTEGER,
	PRIMARY KEY(Id)
);
INSERT INTO `Packages` (Position,Destination) VALUES ('i.P1.R1',3232235625);
INSERT INTO `Packages` (Position,Destination) VALUES ('i.P1.R1',3232235627);
CREATE TABLE `Wires` (
	`Id`	INTEGER NOT NULL UNIQUE,
	`Port1Id`	INTEGER,
	`Port2Id`	INTEGER
);
INSERT INTO `Wires` (Id,Port1Id,Port2Id) VALUES (1,2,4);
INSERT INTO `Wires` (Id,Port1Id,Port2Id) VALUES (2,3,6);