import socket
host = "192.168.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
while True:
 conn, addr = s.accept()
 print addr, "Now Connected"
 conn.send("Thank you for connecting")
 conn.close()
 
 # The while loop keeps the server
#program alive and does not allow the code to end. You can set a connection limit to
#the while loop; for example, set while i>10 and increment i with each connection