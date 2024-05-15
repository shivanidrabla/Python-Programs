# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:06:10 2024

@author: HP
"""

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
average=(num1+num2)/2
dev1=num1-average
dev2=num2-average
print("The average of " ,num1 ," and ", num2, " is ", average)
print("Deviation of ", num1 ," from the average is " ,dev1)
print("Deviation of " ,num2 ," from the average is " ,dev2)

