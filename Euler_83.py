sourceMatrix = []

with open('ProblemFiles/Problem_83.txt') as file:
    for line in file:
        sourceMatrix.append([int(n) for n in line.split(',')])

matrixSize = len(sourceMatrix)
sourceMatrix = [[line[i] for line in sourceMatrix] for i in range(matrixSize)]
cheapestMatrix = [sourceMatrix[0]]

for y in range(1, matrixSize):
    cheapestMatrix[0][y] += cheapestMatrix[0][y-1]

column = 1
prevColumnNeedsUpdate = False

while column < matrixSize:
    prevColumnNeedsUpdate = False
    if len(cheapestMatrix) == column:
        cheapestMatrix.append([sourceMatrix[column][y] + cheapestMatrix[column-1][y] for y in range(matrixSize)])

    for y in range(matrixSize):
        if cheapestMatrix[column-1][y] + sourceMatrix[column][y] < cheapestMatrix[column][y]:
            cheapestMatrix[column][y] = cheapestMatrix[column-1][y] + sourceMatrix[column][y]
    if column != len(cheapestMatrix)-1:
        for y in range(matrixSize):
            if cheapestMatrix[column+1][y] + sourceMatrix[column][y] < cheapestMatrix[column][y]:
                cheapestMatrix[column][y] = cheapestMatrix[column+1][y] + sourceMatrix[column][y]
                prevColumnNeedsUpdate = True
    for y in range(1, matrixSize):
        if cheapestMatrix[column][y-1] + sourceMatrix[column][y] < cheapestMatrix[column][y]:
            cheapestMatrix[column][y] = cheapestMatrix[column][y-1] + sourceMatrix[column][y]
            prevColumnNeedsUpdate = True
    for y in range(matrixSize-2, -1, -1):
        if cheapestMatrix[column][y+1] + sourceMatrix[column][y] < cheapestMatrix[column][y]:
            cheapestMatrix[column][y] = cheapestMatrix[column][y+1] + sourceMatrix[column][y]
            prevColumnNeedsUpdate = True

    if prevColumnNeedsUpdate and column != 0:
        column -= 1
    else:
        column += 1

print(cheapestMatrix[-1][-1])