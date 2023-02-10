# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:28:05 2023

@author: subhash
"""

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        
        print('Bot:','response')