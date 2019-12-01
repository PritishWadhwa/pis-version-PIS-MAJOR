import socket
from speech import *
from constants import *

s = socket.socket()
print "Socket successfully created"


port = SERVER_PORT

s.bind(('', port))
print "socket binded to %s" %(port)

s.listen(NUM_CONN_ALLOWED)
print "listening.."

while True:

   # Establish connection with client.
   c, addr = s.accept()
   print 'Got connection from', addr

   # send a thank you message to the client.
   while True:
       text = speech2text()
       if text:
           c.send(text)
       else:
           pass

   c.close()
