import paho.mqtt.client as mqtt

#host = "localhost"
host="192.168.137.102"

client = mqtt.Client("PublishClient")
#client.username_pw_set("Richard", password="pi")
client.connect(host)

#TODO: Replace this with the values of the measurements
client.publish("test/message", "id=?,naam=?,temp=?,licht=?,vocht=?")

