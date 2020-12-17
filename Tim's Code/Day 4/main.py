import numpy as np
import re

passports = open("passports.txt", "r")
passports = np.array(passports.read().replace('\n\n',',').replace('\n',' ').split(','))

valid_counter = 0
has_cid = False

#Part 1
# for passport in passports:
#   passport = passport.split()

#   for field in passport:
#     if 'cid' in field:
#       has_cid = True

#   if len(passport) == 8 or (len(passport) == 7 and has_cid == False):
#     valid_counter += 1
  
#   has_cid = False

#   print(valid_counter)
#   print('\n')

# print(valid_counter)

#Part 2

def validate(passport):
  is_valid = True

  for field in passport:
    if 'byr' in field:
      val = field.partition('byr:')[2]
      if(not(len(val) == 4 and (1920 <= int(val) <= 2002))):
        is_valid = False
        break
    if 'iyr' in field:
      val = field.partition('iyr:')[2]
      if(not(len(val) == 4 and (2010 <= int(val) <= 2020))):
        is_valid = False
        break
    if 'eyr' in field:
      val = field.partition('eyr:')[2]
      if(not(len(val) == 4 and (2020 <= int(val) <= 2030))):
        is_valid = False
        break
    if 'hgt' in field:
      val = field.partition('hgt:')[2]
      has_cm = 'cm' in val and not 'in' in val
      has_in = 'in' in val and not 'cm' in val
      num = int(re.findall(r'\d+', val)[0])
      if(not((has_cm and num >= 150 and num <= 193) or (has_in and num >= 59 and num <= 76))):
        is_valid = False
        break
    if 'hcl' in field:
      val = field.partition('hcl:')[2]
      if(not(re.match('#[\d|a-f]{6}',val))):
        is_valid = False
        break
    if 'ecl' in field:
      val = field.partition('ecl:')[2]
      if(not(re.match('amb|blu|brn|gry|grn|hzl|oth', val))):
        is_valid = False
        break
    if 'pid' in field:
      val = field.partition('pid:')[2]
      if(not(re.match('\d{9}', val) and len(val) == 9)):
        is_valid = False
        break

  return is_valid


for passport in passports:
  #Divide passport into its fields
  passport = passport.split()

  #check if any of the fields are country ID, set bool accordingly
  for field in passport:
    if 'cid' in field:
      has_cid = True

  if (len(passport) == 8 or (len(passport) == 7 and has_cid == False)) and validate(passport):
    valid_counter += 1
  
  has_cid = False

print(valid_counter)