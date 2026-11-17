# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:10:23 2026

@author: adity
"""

A=int(input("enter angle1 : "))
B=int(input("enter angle2 : "))
C=int(input("enter angle3 : "))
if A+B+C!=180 :
    print("Invalid Triangle")

elif A>90 :
    print("Obtuse angled triangle")
elif A==90 :
    print("Right angled triangle")
else:
    print("Acute angled triangle")