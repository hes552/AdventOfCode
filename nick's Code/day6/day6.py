# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:45:57 2020

@author: Nicholas Smedley
"""
file = open('day6.txt')
quiz_raw = file.read()
quiz = quiz_raw.split("\n\n") 
file.close()

count_all=0
count = 0


for i in range(len(quiz)):
    quiz_first[i] = quiz[i].replace('\n','')
    count = len(set(quiz_first[i]))
    count_all += count
#print(quiz_first)
#print (count_all)
count = 0
count_all = 0
for i in range(len(quiz)):
    quiz[i] = quiz[i].replace('\n',' ')
    quiz[i] = quiz[i].split(' ')
    if len(quiz[i]) == 1:
        count_all += len(set(quiz[i][0]))
    else:
        letters = {}
        for j in range(len(quiz[i])):
            for k in range(len(quiz[i][j])):
                count =''.join(set(quiz[i][j][k]))
                if quiz[i][j][k] in letters:
                    letters[count] += 1
                else:
                    letters[count] = 1
        for key in letters:
            if letters[key] >= len(quiz[i]):
                count_all += 1
                
 
print(quiz)
print(count_all)
