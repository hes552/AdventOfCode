import numpy as np

seat_codes = np.genfromtxt('seats.csv', delimiter='\n', dtype=str)
highest_seat_id = 0
seat_ids = []


#Part 1
# for code in seat_codes:
#   rows = np.arange(128) 
#   cols = np.arange(8)
#   for letter in code:
#     if letter == 'F':
#       rows = np.split(rows,2)[0]
#     elif letter == 'B':
#       rows = np.split(rows,2)[1]
#     elif letter == 'R':
#       cols = np.split(cols,2)[1]
#     else:
#       cols = np.split(cols,2)[0]

#   seat_id = int(rows) * 8 + int(cols)

#   if seat_id > highest_seat_id:
#     highest_seat_id = seat_id

# print(highest_seat_id)

#Part 2

for code in seat_codes:
  rows = np.arange(128) 
  cols = np.arange(8)
  for letter in code:
    if letter == 'F':
      rows = np.split(rows,2)[0]
    elif letter == 'B':
      rows = np.split(rows,2)[1]
    elif letter == 'R':
      cols = np.split(cols,2)[1]
    else:
      cols = np.split(cols,2)[0]

  seat_id = int(rows) * 8 + int(cols)

  seat_ids.append(seat_id)

seat_ids.sort()

for id in range(99,974):
  if seat_ids[id+1] != seat_ids[id]+1:
    print(seat_ids[id] + 1)
    break

