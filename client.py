
import socket
from constants import *

s = socket.socket()
print("in")

port = SERVER_PORT
#ip to connect
s.connect(('192.168.43.41',1101))
while 1:
    sn=s.recv(1024)
    print(sn.decode("utf-8"))
s.close()
