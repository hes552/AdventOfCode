# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:24:37 2020

@author: Holly
"""
import re

file = open("passwords.txt")
expenses = [line.rstrip("\n") for line in file]
file.close()
#print(expenses)
count_old = 0
count = 0
for i in range(0, len(expenses)):
    passwords = re.split(r'[-,:,\s]\s*', expenses[i])
    #if passwords[3].count(passwords[2]) >= int(passwords[0]) and passwords[3].count(passwords[2]) <= int(passwords[1]):
        #print("Valid")
        #print(passwords)
    start = int(passwords[0]) - 1
    end = int(passwords[1]) - 1
    if ((passwords[3][start] == passwords[2]) ^ (passwords[3][end] == passwords[2])):
        print(passwords[3], passwords[0], passwords[1], passwords[2])
        count = count + 1
print(count)
    
