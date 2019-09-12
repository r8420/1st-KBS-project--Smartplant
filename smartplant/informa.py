import paho.mqtt.client as mqtt
import time
import mysql.connector as mariadb
import mysql.connector as errorcode

verbose = True


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected ok")
    else:
        print("not connected")
        sys.exit(2)


# host = "localhost"
host = "192.168.137.102"
client = mqtt.Client("PublishClient")
client.username_pw_set("Richard", password="pi")
client.on_connect = on_connect
client.connect(host)
time.sleep(4)

dbconfig = {
    'user': 'smartplantCMP',
    'password': 'planten',
    'host': 'localhost',
    'raise_on_warnings': True,
}

try:
    mariadb_connection = mariadb.connect(**dbconfig)
    if verbose:
        print("Database connected")

except mariadb.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error: {}".format(err))
    sys.exit(2)
# create the database cursor for executing SQL queries
cursor = mariadb_connection.cursor()
# turn on autocommit
# cursor.autocommit = True
cursor.execute("USE smartplantCMP")
try:
    while True:
        # (buffered = True)
        cursor.execute("SELECT id FROM meting")
        id = cursor.fetchone()[0]
        cursor.execute("SELECT naam FROM meting ")
        measurename = cursor.fetchone()[0]
        print(measurename)
        cursor.execute("SELECT temp FROM meting")
        temp = cursor.fetchone()[0]
        cursor.execute("SELECT vocht FROM meting")
        vocht = cursor.fetchone()[0]
        cursor.execute("SELECT licht FROM meting")
        licht = cursor.fetchone()[0]

        cursor.execute("SELECT naam FROM planten WHERE naam =%s ;", [measurename])
        namePlant = cursor.fetchone()[0]
        cursor.execute("SELECT temp FROM planten WHERE naam =%s ;", [measurename])
        tempPlant = cursor.fetchone()[0]
        cursor.execute("SELECT vocht FROM planten WHERE naam =%s ;", [measurename])
        vochtPlant = cursor.fetchone()[0]
        cursor.execute("SELECT licht FROM planten WHERE naam =%s ;", [measurename])
        lichtPlant = cursor.fetchone()[0]

        tempResult = None
        vochtResult = None
        lichtResult = None

        if measurename == namePlant:
            if temp > tempPlant:
                tempResult = True
            else:
                tempResult = False
            if vocht > vochtPlant:
                vochtResult = True
            else:
                vochtResult = False
            if licht > lichtPlant:
                lichtResult = True
            else:
                lichtResult = False

            sendResult = str.format("id={},naam={},temp={},tempResult={},licht={},vocht={}", id, measurename, temp, tempResult, lichtResult,
                                    vochtResult)
            # TODO: Replace this with the values of the measurements
            client.publish("test/message", sendResult)
            print("result is send")
        else:
            print("plantname does not correspond with any plant in our database.")
            print("for adding a plant, please ask your admin.")

        time.sleep(5)

except KeyboardInterrupt:
    client.disconnect()
