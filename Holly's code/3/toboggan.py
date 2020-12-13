# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:02:15 2020

@author: Holly
"""
file = open("input.txt")
expenses = [line.rstrip("\n")*32 for line in file]
file.close()

across = 0
count = 0
for i in range(0,len(expenses),2):
    print(expenses[i][across])
    if expenses[i][across] == "#":
        count = count + 1
    across = across + 1

print(count)

#r1,d1 77
#r3,d1 280
#r5,d1 74
#r7,d1 78
#r1,d2 35

print(77*280*74*78*35)
