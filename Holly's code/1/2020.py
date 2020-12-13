# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:17:58 2020

@author: Holly
"""

file = open("input.txt")
expenses = [int(line) for line in file]
file.close()
#print(expenses)

for i in range(0, len(expenses)):
    #print(expenses[i])
    for j in range(0, len(expenses)):
        for k in range(0, len(expenses)):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print(expenses[i]*expenses[j]*expenses[k])
                print(expenses[i],expenses[j],expenses[k])

