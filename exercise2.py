# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:09:26 2017

@author: kiran
"""
import timeit
import random
d = {}
for i in range(10000, 1000000, 20000):
    x = list(range(i))
    listdel = timeit.Timer("del(x[%d])"%i,
                              "from __main__ import random, x")
    x1 = {j:None for j in range(i)}
    dicdel = timeit.Timer("del(x1(%d))"%i,
                         "from __main__ import random, x1")

    settime = listdel.timeit(number =10000)
    gettime = dicdel.timeit(number = 10000)
    print("%d, %10.4f, %10.4f" %(i, settime, gettime))