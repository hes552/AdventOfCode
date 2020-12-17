import sys

XMAS_data = open('aoc9_input.txt','r').read()
XMAS_data = XMAS_data.split('\n')

# Part 1
for sum_index in range(25, len(XMAS_data)):
  is_sum = False
  for num1 in range(sum_index-25, sum_index):
    for num2 in range(sum_index-25, sum_index):
      if int(XMAS_data[num1]) == int(XMAS_data[num2]):
        pass
      elif int(XMAS_data[num1]) + int(XMAS_data[num2]) == int(XMAS_data[sum_index]):
        is_sum = True
        break
  if is_sum == False:
    print((XMAS_data[sum_index]))
    break

# Part 2
invalid_num = 1398413738;
total = 0
current_contig_range = []

while total != invalid_num:
  for num in XMAS_data:
    total += int(num)
    current_contig_range.append(int(num))
    if total == invalid_num:
      print(min(current_contig_range) + max(current_contig_range))
      break
    elif total > invalid_num:
      XMAS_data.pop(0)
      current_contig_range = []
      total = 0
      break
    