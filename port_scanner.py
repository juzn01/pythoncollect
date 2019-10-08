#!/usr/binenv python3
import socket
def port_scanner(host,port):
    session = socket.socket()
	try:
	    session.connect((host, port))
		session.settimeout(1.0)
	except:
	    return False
	else:
	    return True
host = input("Enter ip addres or hostname:")
print("{:<20} {:<20} {:<20}.format("Host", "Port", "Status"))
print("{:<20} {:<20} {:<20}.format("-"*20, "-"*20, "-"*20))

for port in range(1, 1025):
    if port_scanner(host,port):
	   print("{:<20} {:<20} {:<20}.format(host, port, "Open"))