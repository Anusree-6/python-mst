# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:09:26 2023

@author: anusree
"""

#A student will not be allowed to sit in exam if his/her attendance is less than 75%

# Get total classes held in school
totalClassesHeld = eval(input("Enter total number of classes held in school : "))

# Get total classes attended by the student
totalClassesAttend = eval(input("Enter total number of classes attended by the student : "))

# Get percent of the attendance
percent = (totalClassesAttend / totalClassesHeld) * 100

# Check if percent is above 75 i.e., eligible to sit in exam or not
if percent < 75:
    print("You cannot sit in the exams as your attendance is too low!")
else:
    print("You can sit in the exams as your attendance is fine.")