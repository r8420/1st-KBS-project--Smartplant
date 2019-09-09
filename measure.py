#!/usr/bin/python3

#
# NAME
#	measure.py - script to store sense hat measurements in SQL database
#
# SYNOPSIS
#	measure.py [-v] [-t interval]
#		-v: verbose
#		-t interval: sample every interval seconds
#
# DESCRIPTION
#	measures temperature data from the raspbery pi sense hat and
#	store data in a local SQL database
#

# import some modules
import sys
import getopt
import sense_hat
import time
import mysql.connector as mariadb
from mysql.connector import errorcode


def stop():
    exit()

# sensor name
sensor_name_1 = 'Temperatuur'
sensor_name_2 = 'Luchtvochtigheid'
sensor_name_3 = 'Licht'
sensor_name_4 = 'Voedingsstoffen'
# database connection configuration
dbconfig = {
    'user': 'richard',
    'password': 'aardappel123',
    'host': 'localhost',
    'database': 'weerstation',
    'raise_on_warnings': True,
}

# parse arguments
verbose = True
interval = 60 # second

try:
    opts, args = getopt.getopt(sys.argv[1:], "vt:")
except getopt.GetoptError as err:
    print(str(err))
    print('measure.py -v -t <interval>')
    print('-v: be verbose')
    print('-t <interval>: measure each <interval> seconds (default: 10s)')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-v':
        verbose = True
    elif opt == '-t':
        interval = int(arg)

# instantiate a sense-hat object
sh = sense_hat.SenseHat()

# infinite loop
try:
    while True:
        # Check if joystick up is active to exit
        for x in sh.stick.get_events():
            if x.direction == 'middle':
                exit()
        # instantiate a database connection
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

        # create the database cursor for executing SQL queries
        cursor = mariadb_connection.cursor(buffered=True)

        # turn on autocommit
        #cursor.autocommit = True

        # get the sensor_id for temperature sensor
        try:
            cursor.execute("SELECT id FROM sensor WHERE naam=%s", [sensor_name_1])
        except mariadb.Error as err:
            print("Error: {}".format(err))
            sys.exit(2)

        sensor_id = [0,1,2]
        sensor_id[0] = cursor.fetchone()
        if sensor_id[0] is None:
            print("Error: no sensor found with naam = %s" % sensor_name_1)
            sys.exit(2)

        if verbose:
            print("Reading data from sensor %s with id %s" % (sensor_name_1, sensor_id[0][0]))

        # get the sensor_id for humidity sensor
        try:
            cursor.execute("SELECT id FROM sensor WHERE naam=%s", [sensor_name_2])
        except mariadb.Error as err:
            print("Error: {}".format(err))
            sys.exit(2)

        sensor_id[1] = cursor.fetchone()
        if sensor_id[1] is None:
            print("Error: no sensor found with naam = %s" % sensor_name_2)
            sys.exit(2)

        if verbose:
            print("Reading data from sensor %s with id %s" % (sensor_name_2, sensor_id[1][0]))

        # measure temperature
        temp = round(sh.get_temperature(), 1)

        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        tempf = float(tFile.read())
        tempC = tempf/1000
        if tempC > 50:
            temp = temp-18.5
        else:
            temp = temp-5

        # print temperature
        sh.set_rotation(180)
        sh.show_message("%.1f C" % temp, scroll_speed=0.10, text_colour=[0, 255, 0])

        # measure humidity
        humidity = round(sh.get_humidity(), 1)


        # verbose
        if verbose:
            print("Temperature: %s C" % temp)
            print("Humidity: %s %%" % humidity)

        # store measurement in database
        try:
            if temp is not 0:
                cursor.execute('INSERT INTO meting (waarde, sensor_id) VALUES (%s, %s);', (temp, sensor_id[0][0]))
            if humidity is not 0:
                cursor.execute('INSERT INTO meting (waarde, sensor_id) VALUES (%s, %s);', (humidity, sensor_id[1][0]))
        except mariadb.Error as err:
            print("Error: {}".format(err))

        else:
            # commit measurements
            mariadb_connection.commit()

            if verbose:
                print("Temperature committed")

            # close db connection
            cursor.close()
            mariadb_connection.close()
            time.sleep(interval)

except KeyboardInterrupt:
    pass
# close db connection
mariadb_connection.close()
# done
