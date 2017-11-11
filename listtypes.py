# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:48:58 2017

@author: kiran
"""

def test1():
    l = []
    for i in range(10):
        l = l + [i]
    return l    

def test2():
    l = []
    for i in range(10):
        l.append(i)
    return l    

def test3():
    return [i for i in range(10)]

def test4():
    l = list[range(10)]
    return l
    
    
print(test1())   

print(test2()) 

print(test3())

print(test4())