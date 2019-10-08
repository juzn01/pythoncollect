import os
import platform
from datetime import datetime
net = raw_input("Enter the Network Address ")
net1= net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(raw_input("Enter the Starting Number "))
en1 = int(raw_input("Enter the Last Number "))
en1=en1+1
oper = platform.system()
if (oper=="Windows"):
 ping1 = "ping -n 1 "
elif (oper== "Linux"):
 ping1 = "ping -c 1 "
else :
 ping1 = "ping -c 1 "
t1= datetime.now()
print "Scanning in Progress"
for ip in xrange(st1,en1):
 addr = net2+str(ip)
 comm = ping1+addr
 response = os.popen(comm)
 for line in response.readlines():
 if(line.count("TTL")):
 break
 if (line.count("TTL")):
 print addr, "--> Live"
t2= datetime.now()
total =t2-t1
print "scanning complete in " , total

#Here, a couple of new things are in the preceding code. The for ip in
#xrange(st1,en1): statement supplies the numeric values, that is, the last octet
#value of the IP address. Within the for loop, the addr = net2+str(ip) statement
#makes it one complete IP address, and the comm = ping1+addr statement makes it a
#full OS command which passes to os.popen(comm). The if(line.count("TTL")):
#statement checks for the occurrence of TTL in the line. If any TTL value is found in the
#line, then it breaks the further processing of the line by using the break statement.
#The next two lines of code print the IP address as live where TTL is found. I used
#datetime.now() to calculate the total time taken to scan.