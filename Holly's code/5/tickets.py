# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:23:30 2020

@author: Holly
"""
file = open("input.txt")
tickets = [line.strip("\n") for line in file]
file.close()
seats = []

for i in range(127):
    print(i)