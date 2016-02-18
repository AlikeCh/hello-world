# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:33:03 2016

@author: alikeche
"""

x = float(raw_input('Enter the number: '))

low = 0.0
high = x

guess = (low + high) / 2

while abs(guess ** 2 - x) > 1e-5:
    if guess ** 2 < x:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2

print 'The root of x is: ', guess