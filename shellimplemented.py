# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:45:00 2017

@author: kiran
"""

def shell(data):
    gap = len(data) // 2
    while gap > 0:
        for k in range(gap):
            gaplist(data,k,gap)
       
        gap = gap //2
    
def gaplist(data,start,gap):
        for i in range(start+gap,len(data),gap):
            
            currentvalue = data[i]
            position = i
            
            while position >= gap and data[position - gap] > currentvalue:
                data[position] = data[position-gap]
                position = position-gap
                
            data[position] = currentvalue   
            
x = [23,34,93,56,12]            
shell(x) 

print(x)           
            
            
            
            