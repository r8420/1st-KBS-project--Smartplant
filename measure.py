#!/usr/bin/python3

#
# NAME
# measure.py - script to store sense hat measurements in SQL database
#
# DESCRIPTION
# measures temperature, humidity and light hours from the raspbery pi sense hat and
# store data in a local SQL database
#

# import some modules
import datetime
import getopt
import sys
import time

import mysql.connector as mariadb
import sense_hat
from mysql.connector import errorcode


def stop():
    exit()


# database connection configuration
dbconfig = {
    'user': 'smartplantCMP',
    'password': 'planten',
    'host': 'localhost',
    'database': 'smartplantCMP',
    'raise_on_warnings': True,
}

# parse arguments
verbose = True
interval = 10  # second

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

try:
    print("Vul de id van deze sensor in:")
    input_id = input()
    cursor.execute("SELECT naam FROM meting WHERE id=%s", [input_id])
except mariadb.Error as err:
    print("Error: {}".format(err))
    sys.exit(2)
row_count = cursor.rowcount
if row_count == 0:

    print("Vul de naam van deze plant in:")
    input_name = input()
    print("Er wordt een sensor voor plant: %s toegevoegd." % input_name)
    try:
        cursor.execute("SELECT naam FROM planten WHERE naam=%s", [input_name])
    except mariadb.Error as err:
        print("Error: {}".format(err))
        sys.exit(2)
    row_count_plant = cursor.rowcount
    if row_count_plant == 0:
        input(
            "[ERROR] Er bestaat nog geen plant met de naam '%s' in de tabel planten. Druk op Enter om toch door te "
            "gaan." % input_name)

    try:
        cursor.execute('INSERT INTO meting (naam, id) VALUES (%s, %s);', (input_name, input_id))
    except mariadb.Error as err:
        print("Error: {}".format(err))
    mariadb_connection.commit()
    print("Success. Selected plant name: %s with id: %d" % (input_name, int(input_id)))

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
        # cursor.autocommit = True

        # measure temperature
        temp = round(sh.get_temperature(), 2)

        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        tempf = float(tFile.read())
        tempC = tempf / 1000
        if tempC > 50:
            temp = temp - 18.5
        else:
            temp = temp - 5
        temp = round(temp, 2)

        # measure humidity
        humidity = round((sh.get_humidity() + 30), 2)
        if humidity > 100:
            humidity = 100

        # calculate light hours
        datetime_now = datetime.datetime.now()
        struct_time_sunrise = time.strptime(datetime.datetime.now().strftime('%Y/%m/%d 07:04:00'), "%Y/%m/%d %H:%M:%S")
        datetime_sunrise = datetime.datetime.fromtimestamp(time.mktime(struct_time_sunrise))

        difference = datetime_now - datetime_sunrise
        light = round(difference.total_seconds() / 3600, 2)

        # verbose
        if verbose:
            print("Temperature: %s C" % temp)
            print("Humidity: %s %%" % humidity)
            print("Light hours: %s hours" % light)

        # store measurement in database
        try:
            cursor.execute('UPDATE meting SET temp=%s, licht=%s, vocht=%s WHERE id=%s;',
                           (temp, light, humidity, input_id))
        except mariadb.Error as err:
            print("Error: {}".format(err))

        else:
            # commit measurements
            mariadb_connection.commit()

            if verbose:
                print("Data committed to database.")

            # close db connection
            cursor.close()
            mariadb_connection.close()
            time.sleep(interval)

except KeyboardInterrupt:
    pass
# close db connection
mariadb_connection.close()
# done
