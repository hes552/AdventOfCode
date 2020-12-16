# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:21:28 2020

@author: Nicholas Smedley
"""

file = open("day5.txt")
boarding = [line.rstrip("\n")for line in file]
file.close()
seat_id = {}

for i in range(len(boarding)):
    row=list(range(128))
    col=list(range(8))
    for j in range(len(boarding[i])):
        if boarding[i][j] == 'F':
            row = row[:len(row)//2]
        elif boarding[i][j] == 'B':
            row = row[len(row)//2:]
        elif boarding[i][j] == 'R':
            col = col[len(col)//2:]
        elif boarding[i][j] == 'L':
            col = col[:len(col)//2]
    seat_id.update({boarding[i] : (row[0]*8)+col[0]})
    


max_id = max(seat_id, key=seat_id.get)
x = seat_id.get(max_id)
print('max id',x)

print('number of passes',len(boarding))
seat_check = list(range(13,881))
seat = list(seat_id.values())    
seat.sort()
#seat = seat.sort()


def non_match_elements(list_a, list_b):
    non_match = []
    for i in list_a:
        if i not in list_b:
            non_match.append(i)
    return non_match
        
 

 
non_match = non_match_elements(seat_check, seat)
print("No match elements: ", non_match)