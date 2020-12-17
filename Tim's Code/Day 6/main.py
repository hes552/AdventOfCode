import numpy as np

customs_answers = open("customs_answers.txt", "r")
customs_answers = np.array(customs_answers.read().replace('\n\n',',').replace('\n',' ').split(','))

grand_total = 0

#Part 1
# for group in customs_answers:
#   group = group.split()
#   yes_answers = []
#   for answers in group:
#     for yes_answer in answers:
#       if yes_answer not in yes_answers:
#         yes_answers.append(yes_answer)
#   group_total = len(yes_answers)
#   grand_total += group_total

# print(grand_total)

#Part 2
for group in customs_answers:
  group = group.split()

  common_yes_answers = set(group[0])

  for answers in range(len(group)):
    answer_set = set(group[answers])
    common_yes_answers = common_yes_answers.intersection(answer_set)

  group_total = len(common_yes_answers)
  grand_total += group_total

print(grand_total)