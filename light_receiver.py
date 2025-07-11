# light_receiver.py
import paho.mqtt.client as mqtt

# MQTT Broker details
broker = "broker.hivemq.com"
port = 1883
topic = "iot/light"

# Callback when message is received
def on_message(client, userdata, msg):
    light_value = msg.payload.decode()
    print(f"💡 Light Intensity Received: {light_value}")

# MQTT client setup
client = mqtt.Client()
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message

print("📥 Waiting for light data on topic 'iot/light'...\n")
client.loop_forever()
