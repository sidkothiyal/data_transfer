import socket
import numpy as np
import os
import io
import pickle
import time

"""
Script to send data, will mostly run on your windows side
"""

TCP_IP = "127.0.0.1"
#TCP_IP = '192.168.0.26' # Change the IP here to that of the ubuntu servert
TCP_PORT = 5006


# Setting up connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while True:
    try:
        arr = [1, 2, 3] # Random data
        print(arr, len(bytearray(arr)))
        arr = bytearray(arr) # Converting it to bytes, because can only send bytes over socket
        length =len(arr) # Finding the size of the byte data
        print(length)
        lengthstr=bytearray(str(length).zfill(8)) # Writing that to a 8 byte number
        # We are finding the number of bytes of the actual data we are going to send and sending that in a defined 8 byte format (hence zfill)
        # This is so that we know exactly how much data to expect on the other end
        s.sendall(lengthstr) #sending byte data
        s.sendall(arr) #sending actual data
        time.sleep(1)
    except Exception as e:
        print ("Error is: ", e)

