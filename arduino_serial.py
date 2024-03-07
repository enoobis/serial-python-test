import serial
import numpy as np

with serial.Serial('COM6', 9600) as ser:
    x = ser.readline()
    print(x)
    
    ser.write("This is my 1st arduino message\n".encode())  # Encode the string to bytes
    
    y = ser.readline()
    print(y)
    
    ser.close()
