# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:58:49 2023

@author: HP
"""

inputFile = "exampletextfile.txt"                        # input text file

N = int(input("Enter N value: "))                        # Enter N value

with open(inputFile, 'r') as filedata:                  # Opening the given file in read-only mode
    linesList= filedata.readlines()                     # Read the file lines using readlines()
print("The following are the first",N,"lines of a text file:")

for textline in (linesList[:N]):                        # Traverse in the list of lines to retrieve the first N lines of a file
    print(textline, end ='')                            # Printing the first N lines of the file line by line.

filedata.close()                                       # Closing the input file