# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:47:59 2023

@author: anusree
"""
#Multiplication Table in Python Using Recursive Function

def rec_multiplication(num,count):
  if( count < 11):
     print(num," * ",count," = ",num * count)
     return rec_multiplication(num,count + 1)
  else:
    return 1
n = int(input("Enter any Number  :"));
rec_multiplication(n,1)