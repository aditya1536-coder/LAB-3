# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:11:52 2026

@author: adity
"""

n=int(input("enter number : "))
d1=n//10000
d2=(n//1000)%10
d3=(n//100)%10
d4=(n//10)%10
d5=n%10

x=d1
position=1

if d2>x:
    x=d2
    position=2

if d3>x:
    x=d3
    position=3
if d4>x:
    x=d4
    position=4
if d5>x:
    x=d5
    position=5
    
print("largest number :" , x)
print("Position : " , position)