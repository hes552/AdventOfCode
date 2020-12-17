adapters = open('aoc_input10.txt','r').read().split('\n')

adapters = sorted(map(int, adapters))
adapters = [0] + adapters


# Part 1
diff_1 = 0
diff_2 = 0
diff_3 = 1 #device_diff
diff_outlet = min(adapters)

if diff_outlet == 1:
  diff_1 += 1
elif diff_outlet == 2:
  diff_2 += 1
elif diff_outlet == 3:
  diff_3 += 1

for adapter in range(0,len(adapters)):
  if adapter + 1 >= len(adapters):
    pass
  elif adapters[adapter] + 1 == adapters[adapter + 1]:
    diff_1 += 1
  elif adapters[adapter] + 2 == adapters[adapter + 1]:
    diff_2 += 1
  elif adapters[adapter] + 3 == adapters[adapter + 1]:
    diff_3 += 1

print(diff_1 * diff_3)

# Part 2
def findPaths(adapters):
  paths = [1] + [0] * (len(adapters)-1)
  for i, adapter in enumerate(adapters):
    for j in range(i - 3, i):
      if(adapter - adapters[j] <= 3):
        paths[i] += paths[j]
  return paths[-1]

print(findPaths(adapters))
