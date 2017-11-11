# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:46:00 2017

@author: kiran
"""

	
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palindrome(string):
    D = Deque()
    for i in string:
        D.addRear(i)
        
    if D.removeFront() == D.removeRear():
        return True
    else: return False    
            
print(palindrome('radar'))    
        