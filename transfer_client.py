import socket
import numpy as np
import os
import io
import pickle
import time

"""
Script to send data, will mostly run on your windows side
"""

TCP_IP = '127.0.0.1' # Change the IP here to that of 
TCP_PORT = 5006

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while True:
    try:
        arr = [1, 2, 3]
        arr = bytes(arr)
        print(arr)
        length =len(arr)
        lengthstr=bytes(str(length).zfill(8), 'utf-8')
        print(lengthstr, len(lengthstr))
        s.sendall(lengthstr)
        s.sendall(arr)
        time.sleep(5)
    except Exception as e:
       print ("Error is: ", e)

