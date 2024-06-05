# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:34:03 2024

@author: teodo
"""



import serial.tools.list_ports
import serial

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)

try:
    ser = serial.Serial('COM9', 115200, timeout=1)
    print("Port opened successfully")
    
    # Read data from the serial port
    data = ser.readline().decode('utf-8').strip()
    print(f"Received data: {data}")

except serial.SerialException as e:
    print(f"Error: {e}")

# Remember to close the port when done
try:
    if ser.is_open:
        ser.close()
        print("Port closed successfully")
except NameError:
    pass


"""
import serial.tools.list_ports
import serial

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)

ser = None

# Try to open each available port
for port in ports:
    port_name = port.device
    try:
        ser = serial.Serial(port_name, 9600, timeout=1)
        print(f"Port {port_name} opened successfully")
        break  # Exit loop once a port is successfully opened
    except serial.SerialException as e:
        print(f"Error: could not open port '{port_name}': {e}")

if ser and ser.is_open:
    # Do something with the open port, then close it
    ser.close()
    print(f"Port {ser.port} closed successfully")
else:
    print("No available ports could be opened.")
"""
