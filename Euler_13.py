import math
print("testing...")

file = open("ProblemFiles/Problem_13.txt",  "r")
numbers = []

for line in file:
    numbers.append(int(line))

file.close()

number = math.fsum(numbers)

while (number > 9999999999):
    number = int(number / 10)

print("solution: ", number)

