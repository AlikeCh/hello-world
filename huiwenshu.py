# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:16:08 2016

@author: alikeche
"""

import math

num = int(raw_input('Input a number: '))

num_r = 0
old = num

flag_huiwen = 0
flag_sushu = 0

for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        break
else:
    flag_sushu = 1
    