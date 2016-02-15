# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:01:15 2016

@author: alikeche
"""

max = 10
sum = 0
extra = 0

for num in range(1,max):
    if num % 2 and not num % 3:
        sum += num
    else:
        extra += 1
        
print extra