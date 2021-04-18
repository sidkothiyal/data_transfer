import socket
import time, os, sys
import rospy
import io, pickle
import struct
import numpy as np

"""
This would be your "server" (from TCP perspective) and would run on your ubuntu system and publish on ROS
"""

TCP_IP = '192.168.0.26' #IP Address of your Ubuntu machine
TCP_IP = "127.0.0.1" # Using this to test both server and client on the same PC
TCP_PORT = 5006 #Any random port you want to use, should be same on both sides
#BUFFER_SIZE = 10000000

# Setting up the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

conn, addr = s.accept()

print("Connected")

# Can init ROS publisher here

while True:
    # try:
        # Initing vars to keep track of how much data is received
        totrec=0 # Bytes received of actual data
        metarec=0 # Bytes receieved of metadata
        msgArray = b'' # For storing actual data
        metaArray = b'' # For storing metadata

        # Going to read metadata now
        while metarec < 8: # Read till all of metadata is received
            chunk = conn.recv(8 - metarec) # To recieve data
            if chunk == '' or chunk is None: # Incase we face an issue
               raise RuntimeError("Socket connection broken")
            metaArray += chunk 
            metarec += len(chunk) 
        metaArray = metaArray.decode() # Received byte data, converting back to int
        max_limit = int(metaArray)
        print(max_limit) # The size of actual data to receive

        # Going to read actual data now
        while totrec < max_limit: 
            chunk = conn.recv(max_limit - totrec)
            if chunk == '' or chunk is None:
               raise RuntimeError("Socket connection broken")
            msgArray += chunk
            totrec += len(chunk)
	    
        # Converting data back to list
        x = list(msgArray.decode())
        for i in range(len(x)):
            x[i] = int(struct.unpack('<B', x[i])[0])
        
        print(x)

        time.sleep(1)

    # except Exception as a:
    #     print ("Error is: ", a)
    #     conn.close()

s.close()
