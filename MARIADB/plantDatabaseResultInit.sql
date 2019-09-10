DROP USER IF EXISTS 'smartplantRES'@'localhost';
DROP DATABASE IF EXISTS smartplantRES;
CREATE DATABASE smartplantRES;
USE smartplantRES;

CREATE TABLE results (
  naam CHAR(20),
  tempC VARCHAR(5),
  temp BOOLEAN,
  licht BOOLEAN,
  vocht BOOLEAN,
  PRIMARY KEY (naam)
);

CREATE USER 'smartplantRES'@'localhost' IDENTIFIED BY 'planten';
GRANT INSERT ON smartplant.planten TO 'smartplantRES'@'localhost';