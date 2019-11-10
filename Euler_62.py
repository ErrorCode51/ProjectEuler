x=10

while True:
    cubesByNumbers = {}
    length = len(str(x**3))
    while len(str(x**3)) == length:
        cube = x**3
        sortedCubeStr = ''.join(sorted(str(cube)))
        if sortedCubeStr not in cubesByNumbers.keys():
            cubesByNumbers[sortedCubeStr] = []
        cubesByNumbers[sortedCubeStr].append(cube)
        x += 1

    cubesWithFiveCubePermutations = []
    for y in cubesByNumbers:
        if len(cubesByNumbers[y]) == 5:
            cubesWithFiveCubePermutations.append(min(cubesByNumbers[y]))

    if cubesWithFiveCubePermutations:
        print('answer:', min(cubesWithFiveCubePermutations))
        break