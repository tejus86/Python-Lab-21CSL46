# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:30:44 2023

@author: HP
"""

sentence = input("Enter a sentence: ")

num_words = len(sentence.split())
num_digits = 0
num_uppercase = 0
num_lowercase = 0

for char in sentence:
    if char.isdigit():
        num_digits += 1
    elif char.isupper():
        num_uppercase += 1
    elif char.islower():
        num_lowercase += 1

print("Number of words:", num_words)
print("Number of digits:", num_digits)
print("Number of uppercase letters:", num_uppercase)
print("Number of lowercase letters:", num_lowercase)

