# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:25:24 2017

@author: kiran
"""

def reverselist(expr):
    if len(expr) == 1:
        return expr[0]
    else: 
        return reverselist(expr[1:]) + expr[0] 
        

print(reverselist('cat'))    