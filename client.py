import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.1" # server address
port =12345 #server port
s.connect((host,port))
print s.recv(1024)
s.send("Hello Server")
s.close()