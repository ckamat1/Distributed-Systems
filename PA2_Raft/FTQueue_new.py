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
        self.__list_of_queues = []
        self.__labelDict = {}

    @replicated
    def incCounter(self):
        self.__list_of_queues.append([])
        return self.__counter

    @replicated
    def qCreate(self,label):
        self.__list_of_queues.append([])
        self.__labelDict[label] = len(self.__list_of_queues)-1
        return self.__labelDict[label]

    @replicated
    def qID(self,label):
        return self.__labelDict[label]




    # @replicated
    # def addValue(self, value, cn):
    #     self.__list_of_queues.append([])
    #     return len(self.__list_of_queues)

    @replicated
    def qPush(self,label, val):
        self.__list_of_queues[label].append(val)
        # return self.__list_of_queues[0]

    @replicated
    def qPop(self,label):
        return self.__list_of_queues[label].pop()

    def getCounter(self):
        return self.__counter

    def getQueue(self):
        if (len(self.__list_of_queues) >= 1):

            return self.__list_of_queues[0]
        else:
            return []

    def getListofQObjects(self):
        if(len(self.__list_of_queues) >= 1):
            return self.__list_of_queues
        else:
            return []


def onAdd(res, err, cnt):
    print("on add called %d" % cnt, res, err)

def onCreate(res,err,cnt):
    print("Queue created for %d" % cnt,res,err)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[1])
    partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]
    print("Before o")
    o = TestObj('localhost:%d' % port, partners)
    n = 0
    old_value = -1
    print("Before while")
    while True:
        # time.sleep(0.005)
        time.sleep(5)
        # nt ("before if value")
        # print(o.getQueue())
        for item in o.getListofQObjects():
            print(item)

        if o._getLeader() is None:
            continue
        # if n < 2000:
        if n < 5:
            o.qCreate(n,callback=partial(onCreate,cnt=n))
            # o.addValue(1, n, callback=partial(onAdd, cnt=n))
        o.qPush(n,10, callback=partial(onAdd, cnt=n))

            # print(len(list_of_queues))
        n += 1
        # if n % 200 == 0:
        # if True:
        #    print('Counter value:', o.getCounter(), o._getLeader(), o._getRaftLogSize(), o._getLastCommitIndex())