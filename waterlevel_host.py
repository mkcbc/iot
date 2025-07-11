# water_tank_monitor.py
import paho.mqtt.client as mqtt
import random
import time

# MQTT Setup
broker = "broker.hivemq.com"
port = 1883
topic_status = "iot/water/status"
topic_motor = "iot/water/motor"

# Create MQTT client
client = mqtt.Client()
client.connect(broker, port)

# Water Level Threshold (in percentage)
CRITICAL_LEVEL = 30  # If level < 30%, motor should start

def simulate_water_level():
    return random.randint(10, 100)  # Simulate tank level (10% to 100%)

print(" Water Tank Monitoring Started...\n")

while True:
    level = simulate_water_level()

    # Check if level is below critical
    if level < CRITICAL_LEVEL:
        motor_status = "ON"
    else:
        motor_status = "OFF"

    # Publish data
    status_msg = f"Water Level: {level}% | Motor: {motor_status}"
    client.publish(topic_status, status_msg)
    client.publish(topic_motor, motor_status)

    print(status_msg)
    time.sleep(3)
