import paho.mqtt.client as mqtt
import time

# MQTT settings
broker = "broker.hivemq.com"
topic = "smartbus/ticketing"

# Define user info
user_id = "passenger_101"
bus_id = "bus_12"

# Connect to MQTT broker
client = mqtt.Client()
client.connect(broker, 1883, 60)

# Simulate sensor detection (e.g., RFID/NFC)
def detect_user_and_send_ticket():
    print("User detected near the bus stop...")
    ticket = {
        "user_id": user_id,
        "bus_id": bus_id,
        "ticket_time": time.ctime(),
        "ticket_status": "valid"
    }
    # Send ticket info as string
    client.publish(topic, str(ticket))
    print("Ticket sent via MQTT:", ticket)

# Simulate system
while True:
    detect_user_and_send_ticket()
    time.sleep(10)  # Send every 10 seconds for demo
