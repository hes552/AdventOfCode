input = []
file = open("input.txt")
for line in file:
    input.append(line.strip("\n").replace("x,",""))
file.close()
print(input)

start = int(input[0])
id = list(map(int,input[1].split(",")))

print(start)
print(id)

lowest_wait = 1000
lowest_id = 0
for i in range(len(id)):
    wait = id[i] - (start % id[i])
    if wait < lowest_wait:
        lowest_wait = wait
        lowest_id = id[i]
print(lowest_id * lowest_wait)
#print(id)