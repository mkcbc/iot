# simulated_rain_alarm.py
import random
import time
import requests

# Simulated weather conditions
weather_options = ["Clear", "Clouds", "Rain", "Drizzle", "Thunderstorm"]

print(" Rain Prediction Monitoring Started...\n")

while True:
    # weather = random.choice(weather_options)
    respnse = requests.get("https://wttr.in/Palghar?format=%C")
    weather = respnse.text
    print(f"Predicted Weather: {weather}")

    if "rain" in weather.lower():
        print(" Rain expected! Triggering alarm...")
        for _ in range(3):
            print(" ALARM: Carry an umbrella!")
            time.sleep(1)
    else:
        print(" No rain predicted.")

    print("\nRechecking in 1 minute...\n")
    time.sleep(60)  # Simulate periodic check
