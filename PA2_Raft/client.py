import socket
import time

while True:
   sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

   sock.connect(('127.0.0.1',6002))
 
   print ("""             1. Create\n
             2. Push\n
             3. Pop\n
             4. Get Queue ID\n
             5. Queue Size\n
             6. Top
             Press any other key to exit 
   Enter your option : 
   """)
   option=int(raw_input())
   if option==1:
       label=raw_input("Enter label : ")
       sock.send("create " + str(label))
   elif option==2:
    label=raw_input("Enter label : ")
    val=raw_input("Enter the value : ")
    sock.send("push "+str(label)+" "+str(val))
    #time.sleep(1)
    message=sock.recv(1024)
    print message
    if message=="False":
      	message="Queue not found"
    else:
      	message="Pushed Successfully!!"
    print message
   elif option==3:
   	qID=raw_input("Enter qID: ")
   	sock.send("pop " + str(qID))
   	
   	message=sock.recv(1024)
   	if message=="False":
   		print("Pop Operation Failed")
   	else:
   		print("The popped element is "+message)
   elif option==4:
   	 label=raw_input("Enter label: ")
   	 sock.send("getqID "+str(label))
   	 time.sleep(1)
   	 message=sock.recv(1024)
   	 if message=="False":
   	 	message="None"
   	 print "The queue ID associated with label " + str(label) + " is " + str(message)
   elif option==5:
      qID=raw_input("Enter qID : ")
      sock.send("getSize "+str(qID))
      time.sleep(1)
      message=sock.recv(1024)
      if message=="False":
      	message="Queue not found"
      else:
      	message="The size of the queue is " + str(message)
      print(message)
   elif option==6:
   	  qID=raw_input("Enter qID : ")
   	  sock.send("qTop "+str(qID))
   	  message=sock.recv(1024)
   	  if message=="False":
   	  	message="Queue not found"
   	  elif message=="noTop":
   	  	message="Queue Empty"
   	  else:
   	  	message="The top element of the queue is " + str(message)
   	  print(message)
   else:
   	print "Bye!!"
   	break
   sock.close()