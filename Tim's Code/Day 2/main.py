import pandas as pd
import numpy as np

#Read file into numpy array
pwds = np.genfromtxt('pwds.csv', delimiter=",", dtype=str)

valid_pwd_count = 0
valid_pwd_count_2 = 0

#Parse data
for pwd_data in pwds:
  #Part 1
  pwd_data = pwd_data.replace(':','')
  pwd_data = pwd_data.split()
  pwd_data[0] = pwd_data[0].split('-')

  min_freq = int(pwd_data[0][0])
  max_freq = int(pwd_data[0][1])
  char = pwd_data[1]
  pwd = pwd_data[2]

  if(pwd.count(char) >= min_freq and pwd.count(char) <= max_freq):
    valid_pwd_count += 1

  #Part 2
  pos_1 = min_freq-1
  pos_2 = max_freq-1

  if((char == pwd[pos_1] and char != pwd[pos_2]) or (char == pwd[pos_2] and char != pwd[pos_1])):
    valid_pwd_count_2 += 1


  
print(valid_pwd_count)
print(valid_pwd_count_2)
