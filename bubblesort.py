# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:59:10 2017

@author: kiran
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


def selectionsort(alist):
    x= []
    y = len(alist)
    for passnum in range(y):
        minval = min(alist)
        x.append(minval)
        alist.remove(minval)
    return x    
    
selectionsort(alist)    
        
        

