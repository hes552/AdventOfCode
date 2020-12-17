boot_code = open('aoc_input8.txt','r').read().split('\n')


# Part 1  
def resolve(boot_code):
  executed_instructions = set()
  instruction_index = 0
  acc = 0

  while instruction_index < len(boot_code):
    if instruction_index in executed_instructions:
      return False, acc
    executed_instructions.add(instruction_index)
    operator = boot_code[instruction_index].split()[0]
    argument = boot_code[instruction_index].split()[1]
    if operator == 'jmp':
      instruction_index += int(argument)
    elif operator == 'acc':
      acc += int(argument)
      instruction_index += 1
    else:
      instruction_index += 1

  return True, acc

print(resolve(boot_code))

# Alternative Less Good Part 1   
# executed_instructions = set()
# instruction_index = 0
# acc = 0

# def execute_instruction(instruction_index, acc):
#   operation = boot_code[instruction_index].split()[0]
#   argument = int(boot_code[instruction_index].split()[1])

#   if instruction_index in executed_instructions:
#     print(acc)
#     return

#   if operation == 'jmp':
#     executed_instructions.add(instruction_index)
#     execute_instruction(instruction_index + argument, acc)
#   elif operation == 'acc':
#     executed_instructions.add(instruction_index)
#     acc += int(argument)
#     execute_instruction(instruction_index + 1, acc)
#   else:
#     execute_instruction(instruction_index + 1, acc)    

# execute_instruction(instruction_index, acc)

# Part 2
for i, line in enumerate(boot_code):
  operator = line.split()[0]
  argument = line.split()[1]
  fixed_boot_code = []
  if operator == 'nop':
    fixed_boot_code = boot_code[:i] + ['jmp ' + argument] + boot_code[i+1:]
  elif operator == 'jmp':
    fixed_boot_code = boot_code[:i] + ['nop ' + argument] + boot_code[i+1:]
  if fixed_boot_code != []:
    resolved = resolve(fixed_boot_code)
    if resolved[0]:
      print(resolved[1])
