sourceMatrix = []

with open('ProblemFiles/Problem_82.txt') as file:
    for line in file:
        sourceMatrix.append([int(n) for n in line.split(',')])

matrixSize = len(sourceMatrix[0])
sourceMatrix = [[line[i] for line in sourceMatrix] for i in range(matrixSize)]

cheapestMatrix = []
cheapestMatrix.append(sourceMatrix[0])


for x in range(1, matrixSize):
    cheapestMatrix.append(sourceMatrix[x].copy())
    for y in range(matrixSize):
        cheapestMatrix[x][y] += cheapestMatrix[x-1][y]
    for y in range(matrixSize):
        for y2 in range(matrixSize):
            if y2 < y:
                if (sum(sourceMatrix[x][y2:(y+1)]) + cheapestMatrix[x-1][y2]) < cheapestMatrix[x][y]:
                    cheapestMatrix[x][y] = (sum(sourceMatrix[x][y2:(y+1)]) + cheapestMatrix[x-1][y2])
            if y2 > y:
                if (sum(sourceMatrix[x][y:(y2+1)]) + cheapestMatrix[x-1][y2]) < cheapestMatrix[x][y]:
                    cheapestMatrix[x][y] = (sum(sourceMatrix[x][y:(y2+1)]) + cheapestMatrix[x-1][y2])

print(min(cheapestMatrix[-1]))