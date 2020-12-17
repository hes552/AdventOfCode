import pandas as pd
input = []
file = open("test.txt")
for line in file:
    input.append(line.strip("\n"))
file.close()
print(input)

#input = "1789,37,47,1889"
temp = input[1].split(",")

id = []
for i in range(len(temp)):
    if temp[i] != "x":
        id.append([int(temp[i]),i])
print(id)

#t = 99999999999988
t = id[0][0]
subsequent = False
mini_subsequent = [0] * len(id)
mini_subsequent[0] = id[0][0]
while not subsequent:
    if t != 0:
        temp_subsequent = True
        for i in range(len(id)):
            if (t + id[i][1]) % id[i][0] != 0:
                temp_subsequent = False
                break
            else:
                if mini_subsequent[i] == 0:
                    mini_subsequent[i] = t
                    #t -= mini_subsequent[i-1]
        print(mini_subsequent)
        if temp_subsequent:
            subsequent = True
            break
    #t = max(mini_subsequent)
    increase = mini_subsequent.copy()
    increase.sort(reverse=True)
    #print(increase)
    #t += increase[0]
    #if t == 0:
    #    t += id[0][0]
    #if increase[1] == 0:
    #    t += id[0][0]
    #else:
    #    t += increase[1]
    #t += mini_subsequent[1]
    t += id[0][0]
    #t += 115318596
print(t)
print(id)
#1068781
