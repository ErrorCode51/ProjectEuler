sourceMatrix = []

with open('ProblemFiles/Problem_82.txt') as file:
    for line in file:
        sourceMatrix.append([int(n) for n in line.split(',')])

sourceMatrix = [[line[i] for line in sourceMatrix] for i in range(80)]

cheapestMatrix = []
cheapestMatrix.append(sourceMatrix[0])


for x in range(1, 80):
    cheapestMatrix.append(sourceMatrix[x].copy())
    for y in range(80):
        cheapestMatrix[x][y] += cheapestMatrix[x-1][y]
    for y in range(80):
        for y2 in range(80):
            if y2 < y:
                if (sum(sourceMatrix[x][y2:(y+1)]) + cheapestMatrix[x-1][y2]) < cheapestMatrix[x][y]:
                    cheapestMatrix[x][y] = (sum(sourceMatrix[x][y2:(y+1)]) + cheapestMatrix[x-1][y2])
            if y2 > y:
                if (sum(sourceMatrix[x][y:(y2+1)]) + cheapestMatrix[x-1][y2]) < cheapestMatrix[x][y]:
                    cheapestMatrix[x][y] = (sum(sourceMatrix[x][y:(y2+1)]) + cheapestMatrix[x-1][y2])

print(min(cheapestMatrix[-1]))