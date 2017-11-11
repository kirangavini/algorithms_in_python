# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:12:39 2017

@author: kiran
"""

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)
     
     def sub(self,otherfraction):
         newnum = self.num*otherfraction.den - self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(abs(newnum),newden)
         return Fraction(newnum//common,newden//common)
     
     def div(self,otherfraction):
         newnum = self.num*otherfraction.den
         newden = self.den*otherfraction.num
         return Fraction(newnum,newden)
     
     def mul(self,otherfraction):
         newnum = self.num*otherfraction.num
         newden = self.den*otherfraction.den
         return Fraction(newnum,newden)
     
     def __greater__(self,otherfraction):
         newnum = self.num/self.den
         newden = otherfraction.num/otherfraction.den
         return newnum > newden
    
     def __less__(self,otherfraction):
         newnum = self.num/self.den
         newden = otherfraction.num/otherfraction.den
         return newnum < newden    
         
     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

x = Fraction(1,2)
y = Fraction(2,3)
print(x.__add__(y))
print(x == y)
print(x.sub(y))
print(x.div(y))
print(x.mul(y))
print(x.__greater__(y))
print(x.__less__(y))
Fraction(1,6).show()
