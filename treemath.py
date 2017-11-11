# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:58:58 2017

@author: kiran
"""

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(expr):
  i= expr.split()
  s = stack()
  tree= binarytree('')
  s.push(tree)
  currenttree = tree
    
  for x in i:    
    if x == '(':
      currenttree.insertLeft('')
      s.push(currenttree)
      currenttree = currenttree.getLeftChild()
            
    elif  x not in ['+','-','*','/']:
      currenttree.setRootvalue(int(i))
      parent = s.pop()
      currenttree = parent
    elif x in ['+','-','*','/']:
      currenttree.setRootvalue(i)  
      currenttree.insertRight('')
      s.push(currenttree)
      currenttree = currenttree.getRightChild()
    elif i == ')': 
      s.pop()  
    else:
        raise ValueError
      
         
  return tree     














t = buildParseTree("( ( 10 + 5 ) * 3 )")