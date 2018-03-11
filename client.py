import time
import datetime
from socket import *

s=socket(AF_INET,SOCK_DGRAM)
oi_di_pair=[]
try:
 serv=raw_input("Enter the IP address : ")
 port=int(raw_input("Enter the port number : "))
 for i in range(0,5):
  time.sleep(1)
  request_time=datetime.datetime.now();
  s.sendto("Sending request...",(serv,port))
  data,addr=s.recvfrom(1024)
  receive_time=datetime.datetime.now();
  send_latency=datetime.datetime.strptime(data.split('\n')[0].split(' : ')[1], "%Y-%m-%d %H:%M:%S.%f")-request_time
  send_latency_milli=send_latency.total_seconds()
  receive_latency=receive_time-datetime.datetime.strptime(data.split('\n')[1].split(' : ')[1], "%Y-%m-%d %H:%M:%S.%f")
  receive_latency_milli=receive_latency.total_seconds()
  delay=abs(receive_latency_milli+send_latency_milli)
  offset=abs(receive_latency_milli-send_latency_milli)/2.00 
  oi_di_pair.append((offset,delay))
 print "(oi,di)\n============\n"
 for x in oi_di_pair:
   print "oi,di  :  " + str(x[0])+','+str(x[1])
except:
  print "Communication Error"
