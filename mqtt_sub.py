import paho.mqtt.client as mqtt
import mysql.connector as mariadb
from mysql.connector import errorcode
import time

#-----------Database stuff--------------

dbconfig = {
    'user': 'smartplantRES',
    'password': 'planten',
    'host': 'localhost',
    'database': 'smartplantRES',
    'raise_on_warnings': True
}

try:
    mariadb_connection = mariadb.connect(**dbconfig)
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
cursor = mariadb_connection.cursor(buffered=True)

#---------End Database stuff---------------

def on_connect(client, userdata, flags, rc):
    print("Connection ", rc)
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Message")
    #Message Format for Database:
    #"id=,naam=,temp=,licht=,vocht="

    #Take the message content from the received message
    message_content = str(message.payload.decode("utf-8"))
    print(message_content)

    #Split it into a list/array of values. E.G. [id=1,temp=37]
    value_list = message_content.split(',')

    #Iterate through the list/array
    for column_data in value_list:
        
        #key is the column name
        key = column_data.split('=')[0]

        #value is the column value
        value = column_data.split('=')[1]

        print("key: %s, value: %s" % (key, value))
        #Insert the values into the database, and if they already exist, update them
        cursor.execute("INSERT INTO result (%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s=%s", (key, value, key, value))

        

    

Connected = False

host="192.168.137.102"
#host = "localhost"
client = mqtt.Client("SubscriberClient")
client.username_pw_set("Richard", password="pi")
client.on_message = on_message
client.on_connect = on_connect
client.connect(host)

client.loop_start()

while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("test/message")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
