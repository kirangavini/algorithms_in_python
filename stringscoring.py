# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:51:09 2017

@author: kiran
"""

import random

def randomalpha(length):
    string = 'abcdefghijklmonpqrstuvwxyz '
    x = ''
    for i in range(0,length):
        x = x + string[random.randrange(27)]
        
    return x
        

def score(goal, string):
    num = 0
    for i in range(0,len(goal)):
       if goal[i] == string[i]:
           num = num + 1
    return float(num/len(goal))    
      


def main():
    y= input('enter your string')
    length = len(y)
    string = randomalpha(length)
    point = 0
    count = 0
    iteration = 0
    while score(y, string) < 1:
        if score(y,string) > point:
            point = score(y,string)
        count = count +1   
        if (count % 100000) == 0:
            iteration = iteration +1
        print(iteration, count ,point, string)    
        string = randomalpha(length)
                
    
     
main()
    
    
    
    
    
    
    
        
    
           
        