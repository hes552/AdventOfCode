# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:46:18 2020

@author: Smushy
"""

file = open("day11.txt")
chairs = [list(line.rstrip("\n"))for line in file]

file.close()


finished = False
while not finished:
    temp_chairs = [x[:] for x in chairs]
    print(temp_chairs)
    for i in range(len(temp_chairs)):
        for j in range(len(temp_chairs[i])):
            adjacent = []
            if i == 0 and j == 0:
                if temp_chairs[i][j + 1]:
                    adjacent.append(temp_chairs[i][j + 1])
                if temp_chairs[i + 1][j]:
                    adjacent.append(temp_chairs[i + 1][j])
                if temp_chairs[i+1][j+1]:
                    adjacent.append(temp_chairs[i+1][j+1])
            elif i == 0 and j == len(temp_chairs[i])-1:
                if temp_chairs[i][j - 1]:
                    adjacent.append(temp_chairs[i][j - 1])
                if temp_chairs[i + 1][j]:
                    adjacent.append(temp_chairs[i + 1][j])
                if temp_chairs[i + 1][j - 1]:
                    adjacent.append(temp_chairs[i + 1][j-1])
            elif i == len(temp_chairs)-1 and j == 0:
                if temp_chairs[i - 1][j]:
                    adjacent.append(temp_chairs[i - 1][j])
                if temp_chairs[i][j + 1]:
                    adjacent.append(temp_chairs[i][j + 1])
                if temp_chairs[i-1][j+1]:
                    adjacent.append(temp_chairs[i-1][j+1])
            elif i == len(temp_chairs)-1 and j == len(temp_chairs[i])-1:
                if temp_chairs[i][j - 1]:
                    adjacent.append(temp_chairs[i][j - 1])
                if temp_chairs[i - 1][j]:
                    adjacent.append(temp_chairs[i - 1][j])
                if temp_chairs[i-1][j-1]:
                    adjacent.append(temp_chairs[i-1][j-1])
            elif i == 0:
                if temp_chairs[i][j + 1]:
                    adjacent.append(temp_chairs[i][j + 1])
                if temp_chairs[i][j - 1]:
                    adjacent.append(temp_chairs[i][j - 1])
                if temp_chairs[i + 1][j]:
                    adjacent.append(temp_chairs[i + 1][j])
                if temp_chairs[i+1][j-1]:
                    adjacent.append(temp_chairs[i+1][j-1])
                if temp_chairs[i+1][j+1]:
                    adjacent.append(temp_chairs[i+1][j+1])
            elif i == len(temp_chairs)-1:
                if temp_chairs[i][j + 1]:
                    adjacent.append(temp_chairs[i][j + 1])
                if temp_chairs[i][j - 1]:
                    adjacent.append(temp_chairs[i][j - 1])
                if temp_chairs[i - 1][j]:
                    adjacent.append(temp_chairs[i - 1][j])
                if temp_chairs[i-1][j-1]:
                    adjacent.append(temp_chairs[i-1][j-1])
                if temp_chairs[i-1][j+1]:
                    adjacent.append(temp_chairs[i-1][j+1])
            elif j == 0:
                if temp_chairs[i + 1][j]:
                    adjacent.append(temp_chairs[i + 1][j])
                if temp_chairs[i - 1][j]:
                    adjacent.append(temp_chairs[i - 1][j])
                if temp_chairs[i][j + 1]:
                    adjacent.append(temp_chairs[i][j + 1])
                if temp_chairs[i-1][j+1]:
                    adjacent.append(temp_chairs[i-1][j+1])
                if temp_chairs[i+1][j+1]:
                    adjacent.append(temp_chairs[i+1][j+1])
            elif j == len(temp_chairs[i])-1:
                if temp_chairs[i + 1][j]:
                    adjacent.append(temp_chairs[i + 1][j])
                if temp_chairs[i - 1][j]:
                    adjacent.append(temp_chairs[i - 1][j])
                if temp_chairs[i][j - 1]:
                    adjacent.append(temp_chairs[i][j - 1])
                if temp_chairs[i-1][j-1]:
                    adjacent.append(temp_chairs[i-1][j-1])
                if temp_chairs[i+1][j-1]:
                    adjacent.append(temp_chairs[i+1][j-1])
            else:
                if temp_chairs[i-1][j-1]:
                    adjacent.append(temp_chairs[i-1][j-1])
                if temp_chairs[i-1][j]:
                    adjacent.append(temp_chairs[i-1][j])
                if temp_chairs[i-1][j+1]:
                    adjacent.append(temp_chairs[i-1][j+1])
                if temp_chairs[i][j-1]:
                    adjacent.append(temp_chairs[i][j-1])
                if temp_chairs[i][j+1]:
                    adjacent.append(temp_chairs[i][j+1])
                if temp_chairs[i+1][j-1]:
                    adjacent.append(temp_chairs[i+1][j-1])
                if temp_chairs[i+1][j]:
                    adjacent.append(temp_chairs[i+1][j])
                if temp_chairs[i+1][j+1]:
                    adjacent.append(temp_chairs[i+1][j+1])
            #print(temp_chairs[i][j])
            #print(adjacent)
            if temp_chairs[i][j] == "L" and adjacent.count("#") == 0:
                #print("occupied")
                chairs[i][j] = "#"
            if temp_chairs[i][j] == "#" and adjacent.count("#") >= 4:
                #print("empty")
                chairs[i][j] = "L"
    if chairs == temp_chairs:
        finished = True
        break
    #print(pd.DataFrame(chairs), "\n")

total = 0
for x in range(len(chairs)):
    total += chairs[x].count("#")
print(total)