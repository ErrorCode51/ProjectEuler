total = 1
currentNumber = 1

for i in range(3, 1002, 2):
    for y in range(4):
        currentNumber += i-1
        total += currentNumber

print(total)