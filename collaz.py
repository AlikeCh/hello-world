# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:05:36 2016

@author: alikeche
"""

for n in range(1,100):
    
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        print n,
            