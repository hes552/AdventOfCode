file = open("easy.txt")
input = [int(line.strip("\n")) for line in file]
file.close()
print(input)

input.sort()
print(input)
'''
input.sort()
adapters = input.copy()
differences = []
current = 0
differences.append(adapters[0]-current)
next = 0
print(adapters)
for i in range(len(adapters)-1):
    current = adapters[i]
    next = adapters[i+1]
    if (next - current) < 4:
        print(next-current)
        differences.append(next - current)
        print(differences)
    else:
        print("Current",current)
        print(differences)
        break
print("Next",next)
print(differences)
print("1",differences.count(1))
print("3",differences.count(3)+1)
print((differences.count(1)) * (differences.count(3)+1))
'''