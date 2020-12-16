# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:45:34 2020

@author: Nicholas Smedley
"""
import copy
file = open("day8.txt")
input = [line.rstrip("\n").split(' ')for line in file]

file.close()


def check(input):
    x= True
    acc = 0
    i = 0
    while x:
        
        
        if input[i][0] == 'nop':     
            
            input[i] = ' '
            i += 1
            if i == len(input):               
                return acc
        if input[i][0] == 'acc':
            
            acc += int(input[i][1])
            print(acc)
            input[i] = ' '
            i += 1
            if i == len(input):                
                return acc            
        if input[i][0] == 'jmp':
            
            temp = int(input[i][1])
            input[i] = ' '            
            i += temp
            if i == len(input):
                
                return acc
        if input[i] == ' ':
            
            return "loop"
        
    

for k in range(len(input)):
    
    
    if input[k][0] == 'jmp':
        b = copy.deepcopy(input)
        b[k][0] ='nop'
        print ("b",b)
        acc = check(b)
        print(acc)
        if acc != "loop":
            break
        
        
    elif input[k][0]=='nop':
        c = copy.deepcopy(input)
        c[k][0] ='jmp'
        print (c)
        acc = check(c)
        print(acc)
        if acc != "loop":
            break
        
    
#print(input)         
print("answer", acc)     
     
