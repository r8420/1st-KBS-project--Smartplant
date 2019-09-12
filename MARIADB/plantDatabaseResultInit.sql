DROP USER IF EXISTS 'smartplantRES'@'localhost';
DROP DATABASE IF EXISTS smartplantRES;
CREATE DATABASE smartplantRES;
USE smartplantRES;

CREATE TABLE results (
  id int not null,
  naam CHAR(20),
  tempC VARCHAR(5),
  temp BOOLEAN,
  licht BOOLEAN,
  vocht BOOLEAN,
  locatie VARCHAR(20),
  foto VARCHAR(50),
  PRIMARY KEY (id)
);

CREATE USER 'smartplantRES'@'localhost' IDENTIFIED BY 'planten';
GRANT INSERT ON smartplantRES.results TO 'smartplantRES'@'localhost';