# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:02:25 2017

@author: kiran
"""

def sumrecursion(numlist):
    if len(numlist) == 1:
        numlist = numlist[0]
    else:
        numlist = numlist[0] + sumrecursion(numlist[1:])
        
    return numlist

print(sumrecursion([1,2,3,4,5,6,7,7,8]))    


def converttostring(number,base):
    characters = "0123456789ABCDEF"
    if number<base:
       return characters[number]
    else:
       return converttostring(number//base, base) + characters[number%base]
       



converttostring(1453,2)       


def reversestring(text):
   size = len(text)-1
   x= ''
   for ch in text:
       x = x + text[size]
       size -= 1
   return x
   
print(reversestring('cat'))   
   
   
    
    

  
                
       