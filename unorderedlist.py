# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:35:44 2017

@author: kiran
"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
        
    def isempty(self):
         return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else: 
                current = current.getNext()
        return found 
        
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else: 
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:    
            previous.setNext(current.getNext())
        
        
        
x = UnorderedList()
x.add(30)
x.add(31)  
x.add(32)  
x.remove(30)
print(x)    
print(x.size())
print(x.isempty())
print(x.search(30))

       