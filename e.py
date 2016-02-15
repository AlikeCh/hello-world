# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:44:50 2016

@author: alikeche
"""

e = 1.0
factorial = 1

for i in range(1,100):
    factorial *= i
    e += 1.0 / factorial

print 'e is ', e