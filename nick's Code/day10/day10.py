# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:48:14 2020

@author: Nicholas Smedley
"""
import itertools 
file = open("simple.txt")
input = [int(line.rstrip("\n"))for line in file]

file.close()

input.sort()
print(input)
one = 1
three = 1
for i in range(len(input)-1):
    if input[i+1] - input[i] == 1:
        one += 1
    if input [i+1] - input[i] == 3:
        three +=1
        
print(one,three)
print(one * three)
perm = 0


    
 

for i in range(len(input)):
    check =[]
    for j in range(i,len(input)):
         check.append(input[j])
print(perm)

