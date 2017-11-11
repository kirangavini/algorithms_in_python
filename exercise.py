# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 20:48:41 2017

@author: kiran
"""

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom
         
     def show(self):
         print(self.num,"/",self.den)   
         
         
         
Fraction(3,8).show()        