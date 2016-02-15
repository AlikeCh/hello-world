# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:49:29 2016

@author: alikeche
"""

pi = 0
sign = 1
divisor = 1

for i in range(1,100000):
    pi += 4.0 * sign / divisor
    sign *= -1
    divisor += 2

print 'pi is ', pi