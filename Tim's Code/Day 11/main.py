import numpy as np

seat_layout = open('aoc_input11.txt','r').read().split('\n')
seat_layout = np.array(seat_layout)
print(seat_layout)




# def applyRules(seat_layout):
#   for i, row in enumerate(seat_layout):
#     for j, seat in enumerate(row):
#       adjacent = [row[i-1][j-1], row[i-1][j], row[i-1][j+1], row[i][j-1], row[i][j], row[i][j+1], row[i-1][j-1], row[i-1][j], row[i-1][j+1]]
#       occ_counter = 0
#       if seat == 'L':
#         if all(adj == 'L' for adj in adjacent):
#           if j-1 < 0 or j+1 > len(row):
#             row[j] == '#'
#       if seat == '#':
#         for adj in adjacent:
#           if adj == '#':
#             occ_counter += 1
#       if occ_counter >= 4:
#         row[j] == 'L'
#   new_seat_layout = seat_layout
#   return new_seat_layout

# print(applyRules(seat_layout))