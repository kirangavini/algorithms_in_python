# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:20:50 2017

@author: kiran
"""
import time
from random import randrange
list = [0, -2, 1, 1, 5, 12, 0.25, 0.15, 9, -3]
def minnumber(list):
    overmin = list[0]
    for i in list:
     issmall = True
     for j in list:
        if i > j:
            issmall = False
     if issmall:
          overmin = i
    return overmin      

def mini(list):
    minsofar = list[0]
    for i in range(len(list)):
     if minsofar > list[i]:
        minsofar = list[i]    
    return minsofar   

#print(mini(list))         
    
    
   
#print(minnumlin(list))            

for listsize in range(1000,10001,1000):
    list = [randrange(10000) for x in range(listsize)]
    start = time.time()
    print(mini(list)) 
    end = time.time()
    print("size: %d time: %f" % (listsize, end-start))