DROP USER IF EXISTS 'smartplantCMP'@'localhost';
DROP DATABASE IF EXISTS smartplantCMP;
CREATE DATABASE smartplantCMP;
USE smartplantCMP;

CREATE TABLE planten(
  naam CHAR(20),
  temp  VARCHAR(5),
  licht VARCHAR(5),
  vocht VARCHAR(5), 
  PRIMARY KEY (naam)
);

CREATE TABLE meting(
  id   int not null,
  naam CHAR(20),
  temp  VARCHAR(5),
  licht VARCHAR(5),
  vocht VARCHAR(5),
  PRIMARY KEY (id)
);

  
INSERT INTO planten (id, naam, temp, licht, vocht) VALUES ('gatenplant', '20', '3,0', '60');
INSERT INTO planten (id, naam, temp, licht, vocht) VALUES ('calathea', '17', '2,0', '50');
INSERT INTO planten (id, naam, temp, licht, vocht) VALUES ('kwartjesplant', '12', '2,0', '55');
INSERT INTO planten (id, naam, temp, licht, vocht) VALUES ('lepelplant','16','2,5','70');
CREATE USER 'smartplantCMP'@'localhost' IDENTIFIED BY 'planten';
GRANT INSERT ON smartplantCMP.planten TO 'smartplantCMP'@'localhost';
