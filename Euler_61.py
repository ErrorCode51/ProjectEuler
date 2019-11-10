from itertools import permutations

def getTriangeNumber(n):
    return int(n*(n+1)/2)

def getSquareNumber(n):
    return n**2

def getPentagonNumber(n):
    return int(n*((3*n)-1)/2)

def getHexagonNumber(n):
    return int(n*((2*n)-1))

def getHeptagonNumber(n):
    return int(n*((5*n)-3)/2)

def getOctagonNumber(n):
    return int(n*((3*n)-2))

polygonNumbers = []
for f in (getTriangeNumber, getSquareNumber, getPentagonNumber, getHexagonNumber, getHeptagonNumber, getOctagonNumber):
    polygonNumbers.append([])
    y = 0
    while True:
        y += 1
        if f(y) > 1000:
            break
    while True:
        pnr = f(y)
        if pnr >= 10000:
            break
        if str(pnr)[2] != '0':
            polygonNumbers[-1].append(pnr)
        y += 1

for f in permutations(polygonNumbers):
    numberSet = []
    for i in range(6):
        numberSet.append([])

    while True:
        isSolution = True

        for y in range(6):
            numberSet[y].clear()
            for x in f[y]:
                if len(numberSet[y-1]) != 0:
                    if str(x)[:2] not in numberSet[y-1]:
                        continue
                if str(x)[2:] not in numberSet[y]:
                    numberSet[y].append(str(x)[2:])

            if len(numberSet[y]) == 0:
                isSolution = False
                break

        if not isSolution:
            break

        if len([x for x in numberSet if len(x) == 1]) == 6:
            numbers = []
            for x in range(6):
                numbers.append(int(numberSet[x-1][0] + numberSet[x][0]))
            print(numberSet)
            print(numbers)
            print('Total:', sum(numbers))
            exit()