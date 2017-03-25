#!/usr/bin/env python
from __future__ import print_function

import sys
import time
from functools import partial
sys.path.append("../")
from pysyncobj import SyncObj, replicated


class TestObj(SyncObj):

    def __init__(self, selfNodeAddr, otherNodeAddrs):
        super(TestObj, self).__init__(selfNodeAddr, otherNodeAddrs)
        self.__counter = 0
        self.__list_of_queues=[]

    @replicated
    def incCounter(self):
        self.__list_of_queues.append([])
        return self.__counter

    @replicated
    def qCreate(self, label):
        self.__list_of_queues.append((label,[]))
        return len(self.__list_of_queues)

    @replicated
    def qPush(self,label,val):
        id=self.getqID(label)
        self.__list_of_queues[id][1].append(val)
        
        return self.__list_of_queues[0]   
    @replicated     
    def qPop(self,label):
         id=self.getqID(label)
         return self.__list_of_queues[id][1].pop(0)
    def getCounter(self):
        return self.__counter

    def getqID(self,label):
        i=0
        for x in range(0,len(self.__list_of_queues)):
             if self.__list_of_queues[x][0]==label:
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

     
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[1])
    partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]
    print ("Before o")
    o = TestObj('localhost:%d' % port, partners)
    n = 0
    old_value = -1
    print ("Before while")
    while True:
        # time.sleep(0.005)
        time.sleep(0.5)
        #nt ("before if value")
        print (o.getQueue())
            

        if o._getLeader() is None:
            continue
        # if n < 2000:
        #if n<5:
        x=raw_input()  
        if x=='create':      
         label=raw_input("Enter your label : ")
         o.qCreate(label, callback=partial(onAdd, cnt=n))
        elif x=='push':
         label=raw_input("Enter your label : ")
         val=raw_input("Enter a value:")
         o.qPush(label,val)
        elif x=='pop':
         label=raw_input("Enter your label : ")
         print("Popped Element is " + str(o.qPop(label)))
        else:
         label=raw_input("Enter your label : ")
         print (o.getqID(label))
        #o.qPush(x, callback=partial(onAdd, cnt=n))
        
            #print(len(list_of_queues))
        n += 1
        # if n % 200 == 0:
        # if True:
        #    print('Counter value:', o.getCounter(), o._getLeader(), o._getRaftLogSize(), o._getLastCommitIndex())
