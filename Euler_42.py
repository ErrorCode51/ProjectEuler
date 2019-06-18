def isTriangleNumber(number):
    i = 1
    while True:
        term = (i/2)*(i+1)
        if term == number:
            return True
        elif term > number:
            return False
        i+=1

def getWordValue(word):
    return sum([ord(c)-96 for c in word.lower()])

total = 0

with open('ProblemFiles/Problem_42.txt') as file:
    for word in file.readline().split(','):
        if isTriangleNumber(getWordValue(word.strip('"'))):
            total += 1

print('total:', total)