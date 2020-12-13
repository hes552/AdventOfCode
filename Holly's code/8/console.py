def check_terminate(temp_console):
    i = 0
    loop = False
    acc = 0
    while not loop:
        if temp_console[i][0] == "acc":
            temp_console[i][2] = int(temp_console[i][2]) + 1
            if int(temp_console[i][2]) > 1:
                loop = True
                #print("acc acc ",acc)
                return "loop"
            #print(int(temp_console[i][1]))
            acc += int(temp_console[i][1])
            i += 1
            if i >= len(temp_console):
                print(acc)
                return "terminate"
                break
        if temp_console[i][0] == "nop":
            temp_console[i][2] = int(temp_console[i][2]) + 1
            if int(temp_console[i][2]) > 1:
                loop = True
                #print("nop acc ",acc)
                return "loop"
            i += 1
            if i >= len(temp_console):
                print(acc)
                return "terminate"
                break
        if temp_console[i][0] == "jmp":
            temp_console[i][2] = int(temp_console[i][2]) + 1
            if int(temp_console[i][2]) > 1:
                loop = True
                #print("jmp acc: ",acc)
                return "loop"
            i += int(temp_console[i][1])
            if i >= len(temp_console):
                print(acc)
                return "terminate"
                break


file = open("input.txt")
console = [(line.strip("\n")+" 0").split(" ") for line in file]
file.close()
#print(console)

temp_console = [x[:] for x in console]

for i in range(len(temp_console)):
    temp_console = [x[:] for x in console]
    if temp_console[i][0] == "jmp":
        temp_console[i][0] = "nop"
        if check_terminate(temp_console) == "terminate":
            break
    elif temp_console[i][0] == "nop":
        temp_console[i][0] = "jmp"
        if check_terminate(temp_console) == "terminate":
            break
#print(console)
#print(acc)
