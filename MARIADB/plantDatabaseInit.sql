DROP USER IF EXISTS 'smartplant'@'localhost';
DROP DATABASE IF EXISTS smartplant;
CREATE DATABASE smartplant;
USE smartplant;
CREATE TABLE planten(
  naam CHAR(20),
  temp CHAR (5),
  licht CHAR(5),
  vocht CHAR(5),
  PRIMARY KEY (naam)
);
INSERT INTO planten (naam, temp, licht, vocht) VALUES ('gatenplant', '20', '3.0', '60');
INSERT INTO planten (naam, temp, licht, vocht) VALUES ('calathea', '17', '2.0', '50');
INSERT INTO planten (naam, temp, licht, vocht) VALUES ('kwartjesplant', '12', '2.0', '55');
INSERT INTO planten (naam, temp, licht, vocht) VALUES ('lepelplant','16','2.5','70');
CREATE USER 'smartplant'@'localhost' IDENTIFIED BY 'planten';
GRANT INSERT ON smartplant.planten TO 'smartplant'@'localhost';
