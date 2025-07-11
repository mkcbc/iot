import time
import random
import winsound

def read_sensor():
    return random.choice([True, False, True, False])

def trigger_alarm():
    print("Alarm Triggered! Motion detected!")
    winsound.Beep(1000, 500)

def reset_system():
    print("System idle. No motion detected.")

def main():
    print("Motion Detection System Simulation\n")
    alarm_triggered = False

    try:
        while True:
            motion = read_sensor()
            if motion:
                if not alarm_triggered:
                    trigger_alarm()
                    alarm_triggered = True
            else:
                if alarm_triggered:
                    reset_system()
                    alarm_triggered = False
                else:
                    print("Monitoring. No motion.")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Simulation stopped.")

if __name__ == "__main__":
    main()
