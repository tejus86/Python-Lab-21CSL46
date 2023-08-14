# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:20:19 2023

@author: HP
"""


def isphonenumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
# call function with a string argument to check if it matches the pattern of a phone number
isphonenumber('415-555-4242')


# How to recognize the same pattern using regular expressions:


import re

number_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

def isphonenumber(number):
    if number_pattern.search(number):
        return True
    else:
        return False
    
isphonenumber('415-555-4242')
