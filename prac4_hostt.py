# player1_host.py
import paho.mqtt.client as mqtt

# Set the secret number
secret_number = 7

# Callback when Player 2 sends a guess
def on_message(client, userdata, msg):
    guess = int(msg.payload.decode())
    print(f"Player 2 guessed: {guess}")

    if guess == secret_number:
        print("Player 2 guessed correctly!")
        client.publish("host/result", "Correct")
    elif guess < secret_number:
        client.publish("host/result", "Too Low")
    else:
        client.publish("host/result", "Too High")

client = mqtt.Client()
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)
client.subscribe("guesser/guess")

print("Host ready. Waiting for guesses...")
client.loop_forever()


# pip install paho-mqtt