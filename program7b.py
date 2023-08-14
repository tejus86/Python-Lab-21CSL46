# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:34:56 2023

@author: HP
"""

class Employee:
    def __init__(self):
        self.name = ""
        self.employee_Id = ""
        self.department = ""
        self.salary = 0
        
    def getEmpDetails(self):
        self.name = input("Enter Employee name : ")
        self.employee_Id = input("Enter Employee ID : ")
        self.department = input("Enter Employee Dept : ")
        self.salary = int(input("Enter Employee Salary : "))
        
    def showEmpDetails(self):
        print("Employee Details")
        print("Name : ", self.name)
        print("ID : ", self.employee_Id)
        print("Dept : ", self.department)
        print("Salary : ", self.salary)
        
    def updtSalary(self):
        self.salary = int(input("Enter new Salary : "))
        print("Updated Salary", self.salary)
        

e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()