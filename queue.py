# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:44:08 2017

@author: kiran
"""



class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def groupelimination(strvalue, shufflenumber):
    S= Queue()
    for val in strvalue:
        S.enqueue(val)
        
    while S.size()>1:
        for i in range(shufflenumber):
            S.enqueue(S.dequeue())
        S.dequeue()
    return S.dequeue()    
    
    
print(groupelimination(["hey","hello","kiran","pen","pencil"], 29))    
             
        
