# device_a.py
import serial
import time

# Connect to COM5 (sending side)
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # Let the connection settle

print("Device A (Sender) is running...")

while True:
    msg = "Hello from Device A\n"
    ser.write(msg.encode())
    print("Sent:", msg.strip())

    # Read response from B (if any)
    if ser.in_waiting:
        response = ser.readline().decode().strip()
        print("Received:", response)

    time.sleep(1)


# device_b.py
import serial

# Connect to COM6 (receiving side)
ser = serial.Serial('COM6', 9600, timeout=1)
print("Device B (Receiver) is running...")

while True:
    if ser.in_waiting:
        msg = ser.readline().decode().strip()
        print("Received:", msg)

        # Echo the message back
        echo_msg = f"Echo: {msg}\n"
        ser.write(echo_msg.encode())
