file = open("input.txt")
input = [int(line.strip("\n")) for line in file]
file.close()
print(input)

preamble_len = 5
preamble = []
for i in range(preamble_len):
    preamble.append(input[i])
print(preamble)

"""
for i in range(preamble_len, len(input)):
    #print(input[i])
    valid = False
    for j in range(len(preamble)):
        for k in range(len(preamble)):
            if preamble[j] + preamble[k] == input[i] and preamble[j] != preamble[k]:
                valid = True
    if not valid:
        print(input[i])
        break
    preamble.pop(0)
    preamble.append(input[i])
"""
target = 400480901
#target = 127
total = 0
contiguous = []
for i in range(len(input)):
    current = input[i]
    total = current
    contiguous = [current]
    if total < target:
        for j in range(i+1, len(input)):
            total += input[j]
            #print("total", total)
            contiguous.append(input[j])
            if total == target:
                #print(contiguous)
                break
            elif total > target:
                #print("large")
                total = 0
                break
    if total == target:
        contiguous.sort()
        print(contiguous[0]+contiguous[-1])
        break

