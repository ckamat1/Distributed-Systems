#!/usr/bin/env python
from __future__ import print_function

import sys
import time
import socket
import thread
from functools import partial
sys.path.append("../")
from pysyncobj import SyncObj, replicated


class TestObj(SyncObj):

    def __init__(self, selfNodeAddr, otherNodeAddrs):
        super(TestObj, self).__init__(selfNodeAddr, otherNodeAddrs)
        self.__counter = 0
        self.__list_of_queues=[]
 

    @replicated
    def qCreate(self, label):
        self.__list_of_queues.append((label,[]))
        return len(self.__list_of_queues)

    @replicated
    def qPush(self,qID,val):
      try:
        if(int(qID)+1>len(self.__list_of_queues)):
            return False
        self.__list_of_queues[int(qID)][1].append(val)
        return True
        
      except:
        return False 


    @replicated     
    def qPop(self,qID):
      try:
        if(int(qID)+1>len(self.__list_of_queues)):
            return False
        result=self.__list_of_queues[int(qID)][1].pop(0)
      except:
            result=False
            return result

   

    def qTop(self,qID):
     try:
      if(int(qID)+1>len(self.__list_of_queues)):
        return False
      else:
        return str(self.__list_of_queues[int(qID)][1][0])
     except:
       return "noTop"


    def qSize(self,qID):
       #try:
        if(int(qID)+1>len(self.__list_of_queues)):
            return False
        else:
            return str(len(self.__list_of_queues[int(qID)][1]))
     #  except:
            return False
 

    def qID(self,label):
        i=0
        for x in range(0,len(self.__list_of_queues)):
             if self.__list_of_queues[x][0]==str(label):
                    return i
             i+=1
        return False

    def getQueue(self):
        if(len(self.__list_of_queues)>=1):

         return self.__list_of_queues
        else:
         return []

def onAdd(res, err, cnt):
 
    print("on add called")

def print_queue(obj):
  while 1:
   command=raw_input("")
   if(command=='print'):
      print (o.getQueue())
   else:
      print("Command not found!!!") 


if __name__ == '__main__':
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('',int(sys.argv[1])))

    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[2])
    partners = ['localhost:%d' % int(p) for p in sys.argv[3:]]
    print ("Before o")
    o = TestObj('localhost:%d' % port, partners)
    n = 0
    old_value = -1
    thread.start_new_thread(print_queue,(o,))
  
    while True:
        # time.sleep(0.005)
        time.sleep(0.5)
        #nt ("before if value")
        if o.getQueue()!=[]:

          print (o.getQueue())
            

        if o._getLeader() is None:
            print ("No Leader!!!")
            continue
        # if n < 2000:
        #if n<5:
        try:
          print ("Current Leader is {}".format(o._getLeader()))
          sock.listen(5)
          conn,caddr=sock.accept()
          print ("hello")
          message=conn.recv(1024)
          x=message.split()[0]
          print (x)
        except:
            continue
        
        if x=='create':    
         label=message.split()[1]  
         #label=raw_input("Enter your label : ")
         o.qCreate(label, callback=partial(onAdd, cnt=n))
        elif x=='push':

         qID=message.split()[1]
         val=message.split()[2]
         mes=o.qPush(qID,val)
         conn.send(str(mes))
         print (mes)
        elif x=='pop':
         #label=raw_input("Enter your label : ")
         print ("Popped")
         qID=message.split()[1]
         try:
           if(int(qID)+1>len(o.getQueue())):
              send=False
           else:
              send=o.getQueue()[int(qID)][1][0]
         except:
              send =False
         print (send)
         conn.send(str(send))
         print("Popped Element is " + str(o.qPop(qID)))
        elif x=='getqID':


         label=message.split()[1]
         conn.send(str(o.qID(label)))
        elif x=='getSize':
            qID=message.split()[1]
            size=o.qSize(qID)
            conn.send(str(size))
        elif x=='qTop':
            qID=message.split()[1]
            top=o.qTop(qID)
            conn.send(str(top))
             
        #o.qPush(x, callback=partial(onAdd, cnt=n))
        
            #print(len(list_of_queues))
     