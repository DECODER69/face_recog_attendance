#!/usr/bin/python

# Test KMtronic WEB Relay board

import serial, time


#Global Variables
ser = 0

#Function to Initialize the Serial Port
def init_serial():
    COMNUM = 3          #Enter Your COM Port Number Here.
    global ser          #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 19200
    ser.port = "COM3"  #COM Port Name Start from 0
    #ser.port = '/dev/ttyUSB0' #If Using  USB-TTL (RS232)
    #ser.port = '/dev/ttyAMA0' # If using RPi Tx and Rx
    #Specify the TimeOut in seconds, so that SerialPort  ""
    #Doesn't hangs
    ser.timeout = 5
    
    #print(ser.port+' is closed.')    
    ser.open()          #Opens SerialPort

    # print port open or closed

        

init_serial()

Status_Request = bytearray(3)
Status_Request[0] = (0xFF)
Status_Request[1] = (0x01)
Status_Request[2] = (0x03)

Command_ON = bytearray(3)
Command_ON[0] = (0xFF)
Command_ON[1] = (0x01)
Command_ON[2] = (0x01)

Command_OFF = bytearray(3)
Command_OFF[0] = (0xFF)
Command_OFF[1] = (0x01)
Command_OFF[2] = (0x00)


# def Status_Check():
#     ser.write(Status_Request)         
#     print (Status_Request)
#     bytes = ser.read(3)     
#     print (bytes)

def Switch_ON():
    ser.write(Command_ON)         
    print (Command_ON)
    bytes = ser.read(3)
    print (bytes)


if ser.isOpen():
    print (('Open: ') + ser.portstr)
    # Switch_ON()
    ser.write(Command_ON[1])
    


# def Switch_OFF():
#     ser.write(Command_OFF)         
#     print (Command_OFF)
#     bytes = ser.read(3)
#     print (bytes)



while 1:
    code = hex('FF 01 01')

    ser.write(code.decode('HEX'))         
    print (Status_Request)
    bytes = ser.read(3)     
    print("goods na")  
    


    exit()
#Ctrl+C to Close Python Window