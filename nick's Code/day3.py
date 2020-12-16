import re

file = open("day3.txt")
map = [line.rstrip("\n")for line in file]
file.close()
#print (map_single)

print(len(map)*7)
print(2261/len(map[0]))

for i in range(0,len(map)):
    map[i] = map[i] *73
count_multi = 1
count_y = 0
count_x = 0
count_tree = 0
while count_y != len(map):
   # print(map[count_y][count_x])
    if (map[count_y][count_x]) == "#":
        count_tree = count_tree + 1
    count_y = count_y + 1
    count_x = count_x + 1
count_multi = count_multi * count_tree
print("1 across",count_tree)

count_y = 0
count_x = 0
count_tree = 0
while count_y != len(map):
   # print(map[count_y][count_x])
    if (map[count_y][count_x]) == "#":
        count_tree = count_tree + 1
    count_y = count_y + 1
    count_x = count_x + 3
count_multi = count_multi * count_tree
print("3 across",count_tree)

count_y = 0
count_x = 0
count_tree = 0
while count_y != len(map):
    #print(map[count_y][count_x])
    if (map[count_y][count_x]) == "#":
        count_tree = count_tree + 1
    count_y = count_y + 1
    count_x = count_x + 5
count_multi = count_multi * count_tree
print("5 across" ,count_tree) 
 
count_y = 0
count_x = 0
count_tree = 0
while count_y != len(map):
    #print(map[count_y][count_x])
    if (map[count_y][count_x]) == "#":
        count_tree = count_tree + 1
    count_y = count_y + 1
    count_x = count_x + 7
count_multi = count_multi * count_tree
print("7 across", count_tree)  

count_y = 0
count_x = 0
count_tree = 0
while count_y <= len(map):
    #print(map[count_y][count_x])
    if (map[count_y][count_x]) == "#":
        count_tree = count_tree + 1
    count_y = count_y + 2
    count_x = count_x + 1
count_multi = count_multi * count_tree
print("1 down", count_tree)
print("multiplying all the values together",count_multi)