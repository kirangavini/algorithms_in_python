# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:04:03 2017

@author: kiran
"""

def coinschange(coinslist,change,mincoins,coinsused):
    for coins in range(change+1):
        coinscount = coins
        newcoin = 0
        for j in [c for c in coinslist if c<= coins]:
            if mincoins[coins - j] + 1 < coinscount:
                coinscount=mincoins[coins - j] +1
                newcoin = j
        mincoins[coins] = coinscount
        coinsused[coins] = newcoin
    return mincoins[change],coinsused

print(coinschange([2,4],10,[0]*11,[0]*11))         
    
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]     