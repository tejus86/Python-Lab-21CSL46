# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:13:50 2023

@author: HP
"""

def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec_rem = binary % 10
        decimal = decimal + dec_rem * pow(2, i)
        binary = binary//10
        i += 1
    print(f"binary number {bin} in decimal is: ", decimal)

bin = int(input("Enter the binary number for conversion: "))
binaryToDecimal(bin)


octal_number = input("Enter octal number")

# convert octal to decimal
decimal_number = 0
power = len(str(octal_number)) - 1
for digit in str(octal_number):
    decimal_number += int(digit) * 8 ** power
    power -= 1

# convert decimal to hexadecimal
hexadecimal_number = hex(decimal_number)[2:].upper()

print(f"The hexadecimal equivalent of {octal_number} is {hexadecimal_number}")
