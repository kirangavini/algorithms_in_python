# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:43:36 2017

@author: kiran
"""

def insertsort(list):    
    for item in range(1,len(list)):
        currentvalue = list[item]
        position = item
        while position > 0 and list[position-1]>currentvalue:
            list[position]=list[position-1]
            position = position -1
        list[position] = currentvalue
       
    return list   
x = [67,34,54,21,46,76]    
print(insertsort(x))
    
    
    
           