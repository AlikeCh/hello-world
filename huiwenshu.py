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
    
while num != 0:
	num_r = num_r * 10 + num % 10
	num = num / 10

if num_r == old:
	flag_huiwen = 1

if flag_huiwen and flag_sushu:
	print old, '既是回文数，又是素数'
else:
	print old, '不是回文+素数'

