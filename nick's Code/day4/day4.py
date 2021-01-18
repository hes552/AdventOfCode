# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:44:10 2020

@author: Smushy
"""
import re
import string
file = open('day4.txt')
passport_raw = file.read()
passport = passport_raw.split("\n\n") 
file.close()

hex= list(string.hexdigits) 


criteria = ['ecl','iyr','hgt','eyr','pid','byr','hcl']
count_valid = 0
info = []
for i in range(len(passport)):
    passport[i] = passport[i].replace('\n',' ')
    if all(x in passport[i] for x in criteria):
        count_valid=count_valid + 1
        passport[i] = passport[i].split(' ')
        info_dict = {}
        for j in range(len(passport[i])):
            #info_dict = {passport[i][j][:3] : passport[i][j][4:]}
            info_dict[passport[i][j][:3]] = passport[i][j][4:]
            #print(info_dict)
        info.append(info_dict)
        
     
#print(info)    
#print (count_valid)
#print (passport)
valid = False
count = 0
for i in range(len(info)):
    for key in info[i]:
        if key == "byr":
            if len(info[i][key]) == 4 and int(info[i][key]) >= 1920 and int(info[i][key]) <= 2002:
                valid = True
            else:
                valid = False
        if key == "iyr":
            if len(info[i][key]) == 4 and int(info[i][key]) >= 2010 and int(info[i][key]) <= 2020:
                valid = True
            else:
                valid = False
        if key == "eyr":
            if len(info[i][key]) == 4 and int(info[i][key]) >= 2020 and int(info[i][key]) <= 2030:
                valid = True
            else:
                valid = False
        if key == "hgt":
            if info[i][key][-2:] == 'cm' and int(info[i][key][:-2]) >= 150 and int(info[i][key][:-2]) <= 193:
                valid = True
            elif info[i][key][-2:] == 'in' and int(info[i][key][:-2]) >= 59 and int(info[i][key][:-2]) <= 76:
                valid = True
            else:
                valid = False
        if key == "hcl":
            if len(info[i][key]) == 7 and any(c in info[i][key][1:] for c in hex) and info[i][key][0] == '#' :
                valid = True
            else:
                valid = False
        if key == "ecl":
            if info[i][key] == 'amb' or info[i][key] == 'blu' or info[i][key] == 'brn' or info[i][key] == 'gry' or info[i][key] == 'grn' or info[i][key] == 'hzl' or info[i][key] == 'oth':
                valid = True
            else:
                valid = False
        if key == "pid":
            if len(info[i][key]) == 9:
                valid = True
            else:
                valid = False
                
        
    if valid:
        count = count + 1
print(count) 
print(count_valid)
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    #hgt (Height) - a number followed by either cm or in:
     #   If cm, the number must be at least 150 and at most 193.
      #  If in, the number must be at least 59 and at most 76.
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    #cid (Country ID) - ignored, missing or not.
