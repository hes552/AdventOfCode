# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:05:53 2020

@author: Holly
"""
file = open("input.txt")
tickets = [line.strip("\n") for line in file]
file.close()
seatID = {}
for i in range(len(tickets)):
    #print(tickets[i])
    row = list(range(128))
    column = list(range(8))
    for j in range(len(tickets[i])):
        if tickets[i][j] == "F":
            row = row[:len(row)//2]
        if tickets[i][j] == "B":
            row = row[len(row)//2:]
        if tickets[i][j] == "L":
            column = column[:len(column)//2]
        if tickets[i][j] == "R":
            column = column[len(column)//2:]
    print(row)
    print(column)
    seatID[tickets[i]] = int(row[0])*8 + column[0]
missing = []
print(seatID)
print(seatID[max(seatID, key=seatID.get)])
{missing.append(value) for key, value in sorted(seatID.items(), key=lambda item: item[1])}
print(missing)

print([i for x, y in zip(missing, missing[1:])for i in range(x + 1, y) if y - x > 1])