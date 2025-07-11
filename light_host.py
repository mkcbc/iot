# simulated_light_sensor.py
import paho.mqtt.client as mqtt
import random
import time

# MQTT Broker Info
broker = "broker.hivemq.com"
port = 1883
topic = "iot/light"

# Connect to MQTT Broker
client = mqtt.Client()
client.connect(broker, port)

print("📡 Simulated Light Sensor Started...\n")

while True:
    # Simulate light value (0 to 1023 like LDR)
    light_value = random.randint(100, 900)

    # Publish to MQTT topic
    client.publish(topic, str(light_value))

    # Print locally
    print(f"Sent light intensity: {light_value}")

    time.sleep(2)  # Send every 2 seconds
