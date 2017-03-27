import socket
import time

while True:
   sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

   sock.connect(('localhost',6003))
 
   print ("""             1. Create\n
             2. Push\n
             3. Pop\n
             Press any other key to exit 
   Enter your option : 
   """)
   option=int(raw_input())
   if option==1:
       label=raw_input("Enter label : ")
       sock.send("create " + label)
   elif option==2:
    label=raw_input("Enter label : ")
    val=raw_input("Enter the value : ")
    sock.send("push "+str(label)+" "+str(val))
   elif option==3:
   	label=raw_input("Enter label: ")
   	sock.send("pop " + str(label))
   else:
   	print "Bye!!"
   	break
   sock.close()