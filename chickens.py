# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:18:25 2016

@author: alikeche
"""

for chickens in range(36):
    for rabbits in range(36):
        if 2 * chickens + 4 * rabbits == 94 and chickens + rabbits == 35:
            print chickens, rabbits
            