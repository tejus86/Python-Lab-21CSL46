# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:36:11 2023

@author: HP
"""

from difflib import SequenceMatcher

string1 = "Python Exercises"
string2 = "Python Exercises"

similarity = SequenceMatcher(None, string1, string2).ratio()

print("Original string:")
print(string1)
print(string2)
print("Similarity between two said strings:")
print(similarity)