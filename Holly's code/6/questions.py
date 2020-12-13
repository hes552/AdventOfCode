file = open("input.txt")
input = [line.strip("\n") for line in file]
file.close()
input.append("")

merging = []
questions = []
for i in range(len(input)):
    if input[i] != "":
        merging.append(i)
    else:
        answers = []
        for j in range(len(merging)):
            answers.append(input[merging[j]])
        questions.append(answers)
        merging = []
print(questions)
total = 0
for i in range(len(questions)):
    #print(questions[i])
    #print(len(set(questions[i])))
    #unique = len(set(questions[i]))
    #total += unique
    matching = 0
    if len(questions[i]) == 1:
        total += len(set(questions[i][0]))
        #print(questions[i])
    else:
        print(questions[i])
        letters = {}
        for j in range(len(questions[i])):
            for k in range(len(questions[i][j])):
                unique = "".join(set(questions[i][j][k]))
                #print(unique)
                if questions[i][j][k] in letters:
                    letters[unique] = letters[unique] + 1
                else:
                    letters[unique] = 1
        print(letters)
        for key in letters:
            print(len(questions[i]))
            if letters[key] >= len(questions[i]):
                total += 1
        #print(matching)
print(total)

#print(total)



