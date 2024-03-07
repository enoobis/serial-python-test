import serial
import time

with serial.Serial('COM6', 9600, timeout=1) as ser:
    time.sleep(2) # Allow time for Arduino to reset after serial connection
    print("Sending activation message to Arduino...")
    ser.write("activate_led\n".encode())  # Send activation command
    time.sleep(5) # Delay to ensure Arduino processes the command

    # You can add more code here if needed
    
    print("Sending deactivation message to Arduino...")
    ser.write("deactivate_led\n".encode())  # Send deactivation command
    time.sleep(1) # Delay to ensure Arduino processes the command
    
    # You can add more code here if needed

    ser.close()
