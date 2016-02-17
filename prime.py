# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:57:14 2016

@author: alikeche
"""

num = int(raw_input('Input a integer number: '))

for i in range(2,num):
    if num % i == 0:
        print num, 'is not the prime!'
        break
else:
    print num, 'is the prime!'