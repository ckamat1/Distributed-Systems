import datetime
from socket import *
import time
data=''
s=socket(AF_INET,SOCK_DGRAM)#Creates a UDP socket
s.bind(('',31000))
while 1:
  data,addr=s.recvfrom(1024)
  request_time=datetime.datetime.now();

  #time.sleep(2)
  reply_time=datetime.datetime.now();
  data="Request time : "+str(request_time)+"\nReply time : "+ str(reply_time)
  s.sendto(data,addr)

