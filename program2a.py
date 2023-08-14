# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:57:40 2023

@author: HP
"""

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input, Please enter a positive integer")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

n = int(input("Enter a positive integer: "))
print(Fibonacci(n))



def fibonacci(n):
    # first two terms
    a, b = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a)
            c = a + b
            # update values of a and b
            a = b
            b = c
            count += 1

# take input from the user
n = int(input("Enter the number of terms: "))
fibonacci(n)