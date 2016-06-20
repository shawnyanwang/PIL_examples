#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import threading
# import time
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print "Starting " + self.name
#
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#
#         threadLock.release()
# x = []
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#         counter -= 1
#         global x
#         x.append(threadName)
#         print x
# threadLock = threading.Lock()
# threads = []
#
#
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
#
# thread1.start()
# thread2.start()
#
#
# threads.append(thread1)
# threads.append(thread2)
#
#
# for t in threads:
#     t.join()
# print "Exiting Main Thread"


#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    i = 1
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        # print "%s processing %d" % (threadName, i)
        i+=1
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
print workQueue
threads = []
threadID = 1


for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1


queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()


while not workQueue.empty():
    pass


exitFlag = 1


for t in threads:
    print t
    t.join()
print "Exiting Main Thread"
