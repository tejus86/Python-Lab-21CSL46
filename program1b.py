# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:49:32 2023

@author: HP
"""

num = int(input("Enter number:"))
temp=num
rev=0
while(num>0):
    dig = num % 10
    rev = rev*10 + dig
    num = num//10
if(temp==rev):
    print(f"The number {temp} is a palindrome!")
else:
    print(f"The number {temp} isn't a palindrome!")
digit_counts = {}
for digit in str(temp):
    if digit in digit_counts:
        digit_counts[digit] += 1
    else:
        digit_counts[digit] = 1
print("Digit counts in", temp, ":")
for digit, count in digit_counts.items():
    print(digit, ":", count)
