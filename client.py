import socket
 
host = '192.168.0.108'
port = 50008

# Username to be sent to the server
user = raw_input("Username: ")
psswd = raw_input("Password to Server: ")

# Connection to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(user)
s.sendall(psswd)

conn_test = s.recv(1024)
if conn_test == "Connection accepted":
	print(conn_test)	
	print("Connected to "+(host)+" on port "+str(port))
	# Initial Message
	initialMessage = raw_input("Initial Message: ")	
	s.sendall(initialMessage) 
	# Messaging loop
	while True:
 		data = s.recv(1024)
 		print("Server: "+(data))
 		response = raw_input("You: ")
 		if response == "exit":
     			break
 		s.sendall(response)
	s.close()
else:
	print(conn_test)
