import random
import time
import winsound 

def get_smoke_level():
    return random.randint(500, 800)  # ppm

def check_fire(smoke):
    if smoke > 600:
        print(f"Smoke Level: {smoke} ppm → Fire Alert! Trigger Alarm.")
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms

    else:
        print(f"Smoke Level: {smoke} ppm → Normal")

def main():
    print("Smoke Detection System\n")
    while True:
        level = get_smoke_level()
        check_fire(level)
        time.sleep(3)

if __name__ == "__main__":
    main()


