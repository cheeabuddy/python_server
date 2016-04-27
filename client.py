import socket
 
host = '192.168.0.108'
port = 50008

# Username to be sent to the server
user = raw_input("Username: ")

# Connection to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connected to "+(host)+" on port "+str(port))
s.sendall(user)

# Initial Message
initialMessage = raw_input("Username: ")
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
