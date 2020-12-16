# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:21:28 2020

@author: Holly
"""
import string

file = open("day4.txt", "r") 
input = file.read()
input = input.split("\n\n")
file.close()
passports = []
for i in range(len(input)):
    input[i] = input[i].replace("\n", " ")
    input[i] = input[i].split(" ")
    passport = {}
    for j in range(len(input[i])):
        passport[input[i][j][:3]] = input[i][j][4:]
    passports.append(passport)
#print(passports)

count = 0
valid = True
for i in range(len(passports)):
    valid = True
    if all(field in passports[i] for field in ("ecl","pid","eyr","hcl","byr","iyr","hgt")): 
        #count = count + 1
        for key in passports[i]:
            if key == "byr":
                if int(passports[i][key]) >= 1920 and int(passports[i][key]) <= 2002:
                    print(passports[i][key])
                    #break
                else:
                    valid = False
            if key == "iyr":
                if int(passports[i][key]) >= 2010 and int(passports[i][key]) <= 2020:
                    print(passports[i][key])
                    #break
                else:
                    valid = False
            if key == "eyr":
                if int(passports[i][key]) >= 2020 and int(passports[i][key]) <= 2030:
                    print(passports[i][key])
                    #break
                else:
                    valid = False
            if key == "hgt":
                if (passports[i][key][-2:] == "cm" or passports[i][key][-2:] == "in") and passports[i][key][:-2].isnumeric():
                    if passports[i][key][-2:] == "cm":
                        if int(passports[i][key][:-2]) >= 150 and int(passports[i][key][:-2]) <= 193:
                            print(passports[i][key])
                            #break
                        else:
                            valid = False
                    if passports[i][key][-2:] == "in":
                        if int(passports[i][key][:-2]) >= 59 and int(passports[i][key][:-2]) <= 76:
                            print(passports[i][key])
                            #break
                        else:
                            valid = False
                else:
                    valid = False
            if key == "hcl":
                if passports[i][key][0] == "#" and all(c in string.hexdigits for c in passports[i][key][1:]):
                    print(passports[i][key])
                    #break
                else:
                    valid = False
            if key == "ecl":
                if passports[i][key] in ("amb","blu","brn","gry","grn","hzl","oth"):
                    print(passports[i][key])
                    #break
                else:
                    valid = False
            if key == "pid":
                if len(passports[i][key]) == 9 and passports[i][key].isnumeric():
                    print(passports[i][key])
                else:
                    valid = False
        if valid == True:
            count = count + 1
                    
print("Count",count)

    