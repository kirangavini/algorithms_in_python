# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:51:39 2017

@author: kiran
"""

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         


def parchecker(string):
    s = Stack()
    n = 0
    
    balenced = True
    while n<len(string) and balenced == True:
        bracket = string[n]
        if bracket in '{[(':
            s.push(bracket)
        else:
            if s.isEmpty():
                balenced = False
            else:
                top = s.pop()
                if not matches(top, bracket):
                    balenced = False
        n = n+1
    if s.isEmpty() and balenced:
        return True
    else: return False    
    
    
def matches(top,bracket):
   opens = '([{'
   close = ')]}'
   return opens.index(top) == close.index(bracket)    
                    


#print(parChecker('{{([][])}()}'))
print(parchecker('[{}]'))
