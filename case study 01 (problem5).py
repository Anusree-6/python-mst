# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 23:13:19 2023

@author: anusree
"""

1.#Python program to find sum of elements in list

total = 0

# creating a list
list1 = [2,6,3,1,5]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]
# printing total value
print("Sum of all elements in given list: ", total)

2.# Python code to split into even and odd lists 
# Funtion to split 
def splitevenodd(A):
    evenlist = [] 
    oddlist = []
    for i in A: 
        if (i % 2 == 0): 
            evenlist.append(i) 
        else: 
            oddlist.append(i) 
    print("Even lists:", evenlist) 
    print("Odd lists:", oddlist)
    
A=list()
n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First  List ::")
for i in range(int(n)):
    k=int(input(""))
    A.append(k)
splitevenodd(A) 
