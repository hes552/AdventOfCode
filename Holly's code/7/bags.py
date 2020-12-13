import string
import re

file = open("input.txt")
input = [line.strip("\n") for line in file]
file.close()
print(input)
bags = {}

for i in range(len(input)):
    input[i] = input[i].translate(str.maketrans('', '', string.punctuation))
    if not any(char.isdigit() for char in input[i]):
        input[i] = input[i].split(" bags")
        #print(input[i][0])
        bags[input[i][0]] = -1
    else:
        input[i] = re.split('contain|bags|bag', input[i])
        input[i] = [j for j in input[i] if j.strip(" ")]
        bags_name = ""
        colours_dict = {}
        for j in range(len(input[i])):
            #print(input[i][j].strip())
            if j == 0:
                bags_name = input[i][j].strip()
            else:
                colours = input[i][j].strip().split(" ")
                colours_dict[colours[1]+" "+colours[2]] = colours[0]
                #print(colours_dict)
            bags[bags_name] = colours_dict
        #print(input[i])
print(bags)
desired_colour = "shiny gold"
next_colour = []
outer_bags = []
growing = True

"""
while growing:
    print("Desired ",desired_colour)
    for key in bags:
        if isinstance(bags.get(key), dict):
            #print("Bag ",key)
            for field in bags[key]:
                #print("Check ",field," against ",desired_colour)
                if field == desired_colour:
                    #print("Match ", key)
                    if key not in outer_bags:
                        outer_bags.append(key)
                        next_colour.append(key)
                        print(next_colour)
    if len(next_colour) == 0:
        break
    desired_colour = next_colour.pop(0)
    print(len(outer_bags))
print(outer_bags)
print(len(outer_bags))
"""

total_dict = {}
final_bags = {}
for key in bags:
    #print(key)
    if not isinstance(bags.get(key), dict):
        print(key,bags.get(key))
        final_bags[key] = 0
print(final_bags)

while True:
    for key in bags:
        count = 0
        total = 0
        print(key)
        if isinstance(bags.get(key), dict):
            for field in bags[key]:
                current_field = ""
                if field in final_bags and key not in final_bags:
                    count += 1
                    current_field = field
                    print(("c",current_field))
                if count == len(bags[key]):
                    #print("b",bags[key].values())
                    #print("f",final_bags)
                    added = []
                    for j in bags[key]:
                        print(final_bags[j])
                        print(final_bags[j],"*",int(bags[key][j]),"=",final_bags[j] * int(bags[key][j]))
                        total += final_bags[j] * int(bags[key][j])
                        added.append(int(bags[key][j]))
                        print(total)
                    for i in range(len(added)):
                        total += added[i]
                    final_bags[key] = total
                    print(final_bags)
    if len(final_bags) == len(bags):
        break

print(final_bags)
print(final_bags["shiny gold"])

