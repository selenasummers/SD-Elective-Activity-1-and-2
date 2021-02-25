import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)
payload = input("Enter message: ")
time.sleep(1)

while True:
    client.loop()
    client.publish("jabagat/message", payload)
    time.sleep(1)
  