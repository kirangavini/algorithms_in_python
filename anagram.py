# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:56:50 2017

@author: kiran
"""

def anagram(s1,s2):
    #listx = [x for x in s2]
    pos1 =0
    ok = True
    if len(s1) != len(s2):
        ok = False
    while pos1<len(s1) and ok:
        pos2 = 0
        found = False
        while pos2<len(s2)and not found:
            if s1[pos1] == s2[pos2]:
               found = True
            else: pos2 = pos2+1
            
        if found:
         ok =True
        else: ok = False
        pos1 = pos1 +1
    return ok    
    
    
def anagramsort(s1,s2):
    pos1 = 0
    s1 = [x for x in s1]
    s2 = [x for x in s2]
    s1.sort()
    s2.sort()
    matches = False
    while pos1 < len(s1) and not matches:
        if s1[pos1] == s2[pos1]:
            pos1 = pos1 +1
            matches = True
        else: matches = False
    return matches   
    
def anagramcount(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    
    for i in range((len(s1))):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos]+1
   
    for i in range((len(s2))):
        pos = ord(s2[i]) - ord('a') 
        c2[pos] = c2[pos]+1
    
    j = 0
    var = True
    while j<26 and var:
        if c1[j] == c2[j]:
            var = True
            j= j+1           
        else: var = False
    return var    
    
print(anagramcount('abcd','dacbq'))