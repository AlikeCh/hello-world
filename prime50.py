# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:10:25 2016

@author: alikeche
"""

x = 2
count = 0

while count < 50:
    for i in range(2, x):
        if x % i == 0:
            break;
    else:
        print x, 'is a prime!'
        count += 1
    x += 1