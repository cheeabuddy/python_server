### PYTHON MODULE CONTAINING FUNCTIONS USED BY SERVER.PY

# Variables


# Functions

def send_message(conn,arg1):
        while (arg1 == True): 
	        message = raw_input("Server: ")
	        if message == "exit":
	       	        arg1 = False;
                else:
		conn.sendall(message)


def recieve_message(conn,user,arg1):
        while (arg1 == True):
	        data = conn.recv(1024)
    	        print((user)+": "+(data))


# Classes
