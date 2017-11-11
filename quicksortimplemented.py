# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:05:44 2017

@author: kiran
"""

def quicksort(alist):
    quicksortfun(alist,0,len(alist)-1)


def quicksortfun(alist,start,end):
     if start < end:
      splitval = partition(alist,start,end)
      
      quicksortfun(alist,start,splitval-1)
      quicksortfun(alist,splitval+1,end)
      
def partition(alist,start,end):
    startval = alist[start]
    
    leftpointer = start+1
    rightpointer =end
    done = False
    
    while not done:
        
    
        while leftpointer <= rightpointer and alist[leftpointer] < startval:
            leftpointer = leftpointer + 1
        
        while rightpointer >= leftpointer and alist[rightpointer] > startval:
            rightpointer = rightpointer -1
        
        
        if rightpointer<leftpointer:
            done = True
        else: 
            temp = alist[rightpointer]
            alist[rightpointer] = alist[leftpointer]
            alist[leftpointer] = temp
            
    temp = alist[start]
    alist[start] = alist[rightpointer]
    alist[rightpointer] = temp
    
    return rightpointer
    
alist1 = [54,26,93,17,77,31,44,55,20]
quicksort(alist1)    
          
         
        