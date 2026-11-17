# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:05:04 2026

@author: adity
"""
x1=float(input("enter x1 : "))
y1=float(input("enter y1 : "))
r=float(input("enter radius : "))

x2=float(input("enter x2 : "))
y2=float(input("enter y2 : "))

distance=((x2-x1)**2 + (y2-y1)**2)*0.5

if distance<r :
    print("Inside")
elif distance==r :
    print("boundary")
else:
    print("Outside")
