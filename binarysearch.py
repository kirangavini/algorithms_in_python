# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:21:43 2017

@author: kiran
"""

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
	
    while first<=last and not found:
        midpoint = (first + last)//2
        y = alist[midpoint]
        if alist[midpoint] == item:
            found = True
        else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
	
    return found
	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 0))
#print(binarySearch(testlist, 13))