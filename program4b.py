# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:04:06 2023

@author: HP
"""

def roman_to_int(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for i in range(len(roman_numeral)-1, -1, -1):
        current_value = roman_dict[roman_numeral[i]]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value
    return result

# Example usage
print(roman_to_int('XXIV')) # Output: 24