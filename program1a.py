# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:34:27 2023

@author: HP
"""

test1 = int(input("Enter marks of Test 1: "))
test2 = int(input("Enter marks of Test 2: "))
test3 = int(input("Enter marks of Test 3: "))
Worst_score = min(test1, test2, test3)
best_average = (test1 + test2 + test3 - Worst_score) / 2  
print("Best average of two tests: ", best_average)
