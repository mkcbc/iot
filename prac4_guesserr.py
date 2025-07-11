# player2_guesser.py
import paho.mqtt.client as mqtt
import time

game_over = False
last_result = ""

def on_message(client, userdata, msg):
    global game_over, last_result
    last_result = msg.payload.decode()
    print("Host:", last_result)
    if last_result == "Correct":
        game_over = True

client = mqtt.Client()
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)
client.subscribe("host/result")

client.loop_start()

while not game_over:
    guess = input("Enter your guess: ")
    client.publish("guesser/guess", guess)
    time.sleep(1) 

client.loop_stop()
print("You won the game!")
