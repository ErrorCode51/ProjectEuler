import string

namelist = []
with open('ProblemFiles/Problem_22.txt') as file:
    namelist += file.read().split(',')

namelist = [i.strip('"') for i in namelist]

namelist.sort()

total = 0
for i in range(len(namelist)):
    name = namelist[i]
    score = 0
    for letter in name:
        score += string.ascii_uppercase.index(letter)+1
    score *= i+1
    total += score
    print(name, ':', score)

print('Total:', total)
