# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:18:59 2023

@author: anusree
"""

#Python program to iterate from start number to the end number and print the sum of the current numberand previous number

previous_num = 0
for i in range(11):
    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i


