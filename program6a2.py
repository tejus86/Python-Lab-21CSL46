# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:03:57 2023

@author: HP
"""

fname = input("Enter file name: ")
word=input("Enter word to be searched:")
k = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                k=k+1
print(f"Occurrences of the word {word} is:" , k )
