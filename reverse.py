# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:29:44 2017

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


def reverse(string):
    s = Stack()
    for i in string:
        s.push(i)
    rev = ''
    while not s.isEmpty():
        rev = rev +s.pop()
        
    return rev   
    
    
def parchecker(string):
    s = Stack()
    balenced = True
    n = 0
    while n<len(string) and balenced:
        if string[n] == '(':
           s.push('(')
        else: 
            if s.isEmpty():
                balenced = False
            else: 
                s.pop()
        n = n + 1
    if s.isEmpty() and balenced:
      return True
    else: return False
        
        
print(parchecker('()'))        
#print(reverse('hello'))       
    