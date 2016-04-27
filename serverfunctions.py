### PYTHON MODULE CONTAINING FUNCTIONS USED BY SERVER.PY

# Variables


# Functions

def send_message(conn):
	message = raw_input("Server: ")
	if message == "exit":
	       	return False;
        else:
		conn.sendall(message)
		return True;

def recieve_message(conn,user):
	data = conn.recv(1024)
    	print((user)+": "+(data))
	return;


# Classes
