from pysyncobj import SyncObj, replicated
from pysyncobj.batteries import ReplList
# import Queue
import sys
from collections import deque
from functools import partial
import time

# # class FTQueue(SyncObj):
# #     listOfQObjects = []
# #     def __init__(self,selfNodeAddr, otherNodeAddrs):
# #         super(FTQueue,self).__init__(selfNodeAddr,otherNodeAddrs)
# #         self.maxSize = 50
# #         # self.qObj = Queue.Queue(self.maxSize)
# #         self.qObj = deque()
# #     # @replicated
# #     # def qCreate(self,label):
# #     #     # global listOfQObjects
# #     #     # self.qObj = Queue.Queue(self.maxSize)
# #     #     #FTQueue.listOfQObjects.append(self.qObj)
# #     #     self.qId = label
# #     #     return self.qId
# #
# #
# #     def qId(self,label):
# #         return label
# #
# #     @replicated
# #     def qPush(self,queue_ID,item):
# #         # global  listOfQObjects
# #         #FTQueue.listOfQObjects[queue_ID].put(item)
# #         self.qObj.append(item)
# #
# #     @replicated
# #     def qPop(self,queue_ID):
# #         # global listOfQObjects
# #         #qObj = FTQueue.listOfQObjects[queue_ID]
# #         try:
# #             item = self.qObj.pop()
# #         except Exception as e:
# #             return e
# #
# #         return item
# #
# #     def qTop(self,queue_ID):
# #         # global listOfQObjects
# #         #qObj = FTQueue.listOfQObjects[queue_ID]
# #         # qObj1 = self.qObj
# #         if not self.qObj:
# #             return self.qObj[0]
# #         return None
# #
# #     def qSize(self,queue_ID):
# #         # global listOfQObjects
# #         # qObj1 = self.qObj
# #         # size = qObj1.qsize()
# #         size = self.qObj.qsize()
# #         return size
# #
# #     def display(self):
# #         print self.qObj
#
# class FTQueue():
#     queue_ID = 0
#     def __init__(self):
#         FTQueue.queue_ID += 1
#         self.queueId = FTQueue.queue_ID
#         self.q = deque()
#
#
#
#
# class helperQ(SyncObj,FTQueue):
#     def __init__(self,selfNodeAddr, otherNodeAddrs):
#         super(FTQueue, self).__init__(selfNodeAddr, otherNodeAddrs)
#         self.listOfQueues = []
#         self.labelDict = {}
#
#     @replicated
#     def qCreate(self,label):
#         obj = FTQueue()
#         self.labelDict[label] = obj.queueId
#         self.listOfQueues.append(obj)
#
#     def qID(self,label):
#         return self.labelDict[label]
#
#     @replicated
#     def qPush(self,label,item):
#         id = self.qID(label)
#         FTqObj = self.listOfQueues[id]
#         FTqObj.q
#
#
#     def qPop(self, ):








def create(res,err,label):
    print("Created a queue for label {}".format(label),res,err)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[1])
    partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]
    q = ReplList()
    sync = SyncObj('localhost:%d' % port,partners,consumers=[q])
    # for item in range(5):
    #     q.append(item)
    while True:
        q.insert(0,10)
        print q.rawData()
        time.sleep(10)

    # q.remove(4)
    # print q.rawData()





































    # q = FTQueue('localhost:{}'.format(port),partners)
    # num_clients = 3
    # label = 0
    # # while num_clients > 0:
    # #     ID = q.qCreate(label)
    # #     q.qPush(ID,1)
    # #     q.qPush(ID,2)
    # #     q.qPush(ID,3)
    # #listOfQObjects = []
    #
    # # q.qCreate(0,callback=partial(create,label=0))
    # #listOfQObjects.append(q)
    # #print ID
    # ID = q.qId(0)
    # # print ID
    # q.qPush(ID,1)
    # q.qPush(ID,2)
    # q.qPush(ID,3)
    # #print q.qPop()
    # q.display()
    #


