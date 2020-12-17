import numpy as np
import pandas as pd

hill = np.genfromtxt('map.csv', delimiter=",", dtype = str, comments = '~')

x_pos = 0
y_pos = 0
gradients = np.array([[1,1],[3,1],[5,1],[7,1],[1,2]])
tree_count = 0
tree_prod = 1

for gradient in gradients:
  x_pos = 0
  y_pos = 0

  change_in_x = gradient[0]
  change_in_y = gradient[1]

  for row in hill:

    if(y_pos + change_in_y > 323):
      break

    if(hill[y_pos][x_pos] == '#'):
      tree_count += 1
    
    if x_pos + change_in_x > 30:
      x_pos -= 31
    
    x_pos += change_in_x
    y_pos += change_in_y

  tree_prod *= tree_count
  tree_count = 0

print(tree_prod)