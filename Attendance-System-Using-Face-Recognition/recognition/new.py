import serial
import time

ser = serial.Serial(
    port='COM3',
    baudrate=9600,

    timeout=10
    )
#tried this
cw = [0x01]

ser.write(serial.to_bytes(cw))

#tried this
cw = [0x00]
ser.write(serial.to_bytes(cw))
