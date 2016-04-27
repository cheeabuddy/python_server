import socket

host = '192.168.0.108'
port = 50008

# Server startup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# Waiting for connection
s.listen(1)
conn, addr = s.accept()
user = conn.recv(1024)
print ("Connection from", addr, "Username: ",user)

# Messaging loop
while True:
    data = conn.recv(1024)
    if not data: break
    print(user,": "+(data))
    response = raw_input("Server: ")
    if response == "exit":
        break
    conn.sendall(response)
conn.close()
