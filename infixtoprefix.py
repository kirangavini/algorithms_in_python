# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:19:37 2017

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

def infixtopostfix(expr):
    operations = {}
    operations["*"] = 3
    operations["+"] = 2
    operations["-"] = 2
    operations["("] = 1
    finalist = []
    S = Stack()
    exprsplit = expr.split()
    
    for token in exprsplit:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            finalist.append(token)
        elif (token == '('):
              S.push(token)   
        elif (token == ')'):
             toptoken = S.pop()
             while toptoken != '(':
                finalist.append(toptoken)
                toptoken = S.pop()                                           
        else:
            while( not S.isEmpty()) and (operations[S.peek()] >= operations[token]) :
                finalist.append(S.pop())
            S.push(token)
          
    while not S.isEmpty():
         finalist.append(S.pop())
    return " ".join(finalist)

print(infixtopostfix("A * B + C * D"))        
    