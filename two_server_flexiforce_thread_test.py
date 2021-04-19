import time
import threading
from math import sqrt
from random import randint
import os
import sys

while(1):
    #if not os.isatty(sys.stdin.fileno()):
    #print (sys.stdin.readline())
    #else:
    print(sys.stdin.readline(), flush=True)
    print ("Skip, so it doesn't hang")


# def findPrimes(aList):
#     for testValue in aList:
#         isPrime = True
#         for i in range(2,int(sqrt(testValue)+1)):
#             if testValue % i == 0:
#                 isPrime = False
#         if isPrime:
#             #print(testValue)
#             pass
# 
# testValues1 = []
# testValues2 = []
# for i in range(1000):
#     testValues1.append(randint(10,100))
#     testValues2.append(randint(10,100))
# 
# 
# t = time.process_time()
# findPrimes(testValues1)
# findPrimes(testValues2)
# print('The long way',time.process_time() - t) # runs in 0.006 to 0.007
# 
# 
# t = time.process_time()
# thread1 = threading.Thread(target=findPrimes(testValues1))
# thread2 = threading.Thread(target=findPrimes(testValues2))
# thread1.start()
# thread2.start()
# print('The threading way',time.process_time() - t) # also runs in 0.006 to 0.007
