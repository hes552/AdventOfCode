# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:00:27 2020

@author: Nicholas Smedley
"""

file = open("day9_test.txt")
input = [int(line.rstrip("\n"))for line in file]

file.close()


"""
bad_num = 0                               
preamble_len =5
preamble = []        
for i in range(preamble_len):
    preamble.append(input[i])
print(preamble)
for i in range(preamble_len,len(input)):
    valid = False
    for j in range(preamble_len):
        for k in range(preamble_len):
            if int(preamble[j]) +int(preamble[k]) == input[i]: #and preamble[j] != preamble[k]:
                valid = True
    if not valid:
        bad_num =input[i]
        print(input[i],'bad')
        break
    preamble.pop(0)
    preamble.append(input[i])
"""
for i in range(len(input)):
    check =[]
    for j in range(i,len(input)):
        check.append(input[j])
        
        if sum(check) == 127:
            print(sum(check))
            print(min(check) + max(check))
            
      
    
