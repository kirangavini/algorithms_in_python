# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 00:10:02 2017

@author: kiran
"""

def mergesort(alist): 
    if len(alist)>1:
        midpoint = len(alist) // 2
        leftlist = alist[:midpoint]
        rightlist = alist[midpoint:]
        mergesort(leftlist)
        mergesort(rightlist)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k]= leftlist[i]
                i =i +1
            else: 
                alist[k] = rightlist[j]
                j=j+1
            k = k+1
            
        while i < len(leftlist):
            alist[k] = leftlist[i]
            k = k+1
            i = i+1

        while j < len(rightlist):
            alist[k] = rightlist[j]
            k = k +1
            j = j +1
list = [23,12,34,45,32,11,98,31]    
mergesort(list)             
        
    