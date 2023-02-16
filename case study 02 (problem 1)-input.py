# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:05:11 2023

@author: anusree
"""

#to sum all the numbers in a list

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((25, 16, 3, 9, 8)))


