sourceMatrix = []

with open('ProblemFiles/Problem_81.txt') as file:
    for line in file:
        sourceMatrix.append([int(n) for n in line.split(',')])

matrixSize = len(sourceMatrix)
sourceMatrix = [[line[i] for line in sourceMatrix] for i in range(matrixSize)]
cheapestMatrix = [sourceMatrix[0]]

for y in range(1, matrixSize):
    cheapestMatrix[0][y] += cheapestMatrix[0][y-1]

for x in range(1, matrixSize):
    cheapestMatrix.append(sourceMatrix[x].copy())
    for y in range(matrixSize):
        cheapestMatrix[x][y] += cheapestMatrix[x-1][y]
    for y in range(1, matrixSize):
        if cheapestMatrix[x-1][y] > cheapestMatrix[x][y-1]:
            cheapestMatrix[x][y] = cheapestMatrix[x][y-1] + sourceMatrix[x][y]

print(cheapestMatrix[-1][-1])