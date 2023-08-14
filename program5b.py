# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:33:27 2023

@author: HP
"""

with open('filename.txt', 'r') as file:
    text = file.read()
import re
# Search for phone numbers using regular expressions
phone_numbers = re.findall(r'\+91\d{10}', text)

# Search for email addresses using regular expressions
email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Print the results
print("Phone numbers found:", phone_numbers)
print("Email addresses found:", email_addresses)