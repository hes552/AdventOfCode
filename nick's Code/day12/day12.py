# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:09:51 2021

@author: Smushy
"""

file = open("day12.txt")
input = [line.rstrip("\n")for line in file]
file.close()
print(input)
count_ns = 0
count_ew = 0
count_rot = 90
waypoint_ns = 1
waypoint_ew = 10
waypoint_rot = 90
for i in range(len(input)):
    if input[i][0] == 'N':
        waypoint_ns += int(input[i][1:])
    if input[i][0] == 'S':
        waypoint_ns -= int(input[i][1:])
    if input[i][0] == 'E':
        waypoint_ew += int(input[i][1:])
    if input[i][0] == 'W':
        waypoint_ew -= int(input[i][1:])
    if input[i][0] == 'R':
        turn = int(int(input[i][1:])/90)
        for j in range(turn):
            temp = waypoint_ns
            waypoint_ns = -(waypoint_ew)
            waypoint_ew = temp
        waypoint_rot += int(input[i][1:])
        count_rot = waypoint_rot%360
    if input[i][0] == 'L':
        turn = int((360 - int(input[i][1:]))/90)
        for j in range(turn):
            temp = waypoint_ns
            waypoint_ns = -(waypoint_ew)
            waypoint_ew = temp        
        waypoint_rot -= int(input[i][1:])
        waypoint_rot = waypoint_rot%360
    if input[i][0] == 'F':
        count_ns += int(input[i][1:]) * waypoint_ns
        count_ew += int(input[i][1:]) * waypoint_ew
    
    print(count_ns,count_ew,count_rot)    
x= abs(count_ns) + abs(count_ew)
print(x)   

