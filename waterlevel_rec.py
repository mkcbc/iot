# water_receiver.py
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f" Update: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)
client.subscribe("iot/water/status")
client.on_message = on_message

print("Monitoring water tank level...\n")
client.loop_forever()
