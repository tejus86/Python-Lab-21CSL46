# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:59:18 2023

@author: HP
"""

import os
from zipfile import ZipFile

# Create object of ZipFile
with ZipFile('E:/Zipped file.zip', 'w') as zip_object:
   # Traverse all files in directory
   for folder_name, sub_folders, file_names in os.walk('E:\CIT\DSD lab programs'):
      for filename in file_names:
         # Create filepath of files in directory
         file_path = os.path.join(folder_name, filename)
         # Add files to zip file
         zip_object.write(file_path, os.path.basename(file_path))

if os.path.exists('E:/Zipped file.zip'):
   print("ZIP file created")
else:
   print("ZIP file not created")