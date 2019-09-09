#!/usr/bin/python3

import sys
import sense_hat
import mysql.connector as mariadb
from mysql.connector import errorcode

# database connection configuration
dbconfig = {
    'user': 'sensem',
    'password': 'h@',
    'host': 'localhost',
    'raise_on_warnings': True,
}

verbose = False

try:
    mariadb_connection = mariadb.connect(**dbconfig)
    if verbose:
        print("Database connected")

except mariadb.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error: {}".format(err))
    sys.exit(2)

cursor = mariadb_connection.cursor(buffered=True)
try:
    cursor.excute('CREATE DATABASE smartplant;')
    cursor.excute('USE smartplant;')
    cursor.excute('CREATE TABLE info ('
                  'name CHAR(20), temp CHAR (4), licht CHAR(10), vocht CHAR(5), ')

except mariadb.Error as err:
    print("Error: {}".format(err))
