# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:55:09 2016

@author: alikeche
"""

points = int(raw_input('Leading points: '))
has_ball = raw_input('The leading team has ball (yes/no)')
seconds = float(raw_input('The remaining seconds: '))

points -= 3

if has_ball == 'yes' or has_ball == 'Yes':
    points += 0.5
else:
    points -= 0.5

if points < 0:
    points = 0

points **=2

if points > seconds:
    print 'Safe'
else:
    print 'Not safe'