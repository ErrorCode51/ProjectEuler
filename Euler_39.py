nrOfSolutions = 0
value = 0

for x in range(3, 1001):
    print(x)
    solutions = 0
    for y in range(1, x-1):
        for z in range(1, y):
            if (y**2) + (z**2) == ((x-y-z)**2):
                solutions += 1
            elif (y**2) + (z**2) > ((x-y-z)**2): # performance
                break
    if solutions > nrOfSolutions:
        nrOfSolutions = solutions
        value = x

print('value:', value)
print('solutions:', nrOfSolutions)