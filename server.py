
# Importing modules
import socket
import thread
from serverfunctions import *

# Global variables
running = True;


host = '192.168.0.108'
port = 50008

# Server startup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# Waiting for connection
s.listen(1)
conn, addr = s.accept()
user = conn.recv(1024)
psswd = conn.recv(1024)

if psswd == 'pi':
	conn.sendall("Connection accepted")
	print ("Connection from: " + (str(addr[0])) + "\nUsername: " + (user))

	# Messaging loop
        # Create two threads as follows
        try:
                thread.start_new_thread( recieve_message, (conn,user,running) )
                thread.start_new_thread( send_message, (conn,running ) )
        except:
                print "Error: unable to start thread"
else:
	print ("Connection refused")
	print ("Shutting down")
        conn.sendall("Connection refused")
	conn.close()
