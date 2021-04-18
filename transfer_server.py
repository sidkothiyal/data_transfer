import socket
import time, os, sys
#import rospy
import io, pickle
import numpy as np

TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 10000000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

conn, addr = s.accept()

while True:
    try:    
        totrec=0
        metarec=0
        msgArray = b''
        metaArray = b''
        while metarec < 8:
            chunk = conn.recv(8 - metarec)
            if chunk == '' or chunk is None:
               raise RuntimeError("Socket connection broken")
            metaArray += chunk
            metarec += len(chunk) 
        metaArray = metaArray.decode("utf-8")
        max_limit = int(metaArray)
        print(max_limit)

        while totrec < max_limit:
            chunk = conn.recv(max_limit - totrec)
            if chunk == '' or chunk is None:
               raise RuntimeError("Socket connection broken")
            msgArray += chunk
            totrec += len(chunk) 
        print(list(msgArray))
        time.sleep(5)
        
    except Exception as a:
        print ("Error is: ", a)
        conn.close()

s.close()