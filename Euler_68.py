import itertools

solutionStringList = []

for i in itertools.permutations(range(1, (2*5)+1)):
    if i.index(10)%2 == 1:
        continue # If the index of 10 is odd, the polygon will result in a 17 character string
    polygon = [i[x-1:x+1] for x in range(1, (2*5)+1, 2)]
    # Calculate the sum of the first side
    total = sum(polygon[0])+polygon[-1][1]
    solutionSet = [int(''.join(map(lambda n: str(n), polygon[0]+(polygon[-1][1],)))),]

    for p in range(1, 5):
        if sum(polygon[p])+polygon[p-1][1] != total:
            break # Sides do not all have the same total, the polygon in isvalid
        solutionSet.append(int(''.join(map(lambda n: str(n), polygon[p]+(polygon[p-1][1],)))))

    if len(solutionSet) == 5: # If the side all have the same total
        solutionSet.reverse() #The polygon is iterated couterclockwise, the solution is clockwise
        while solutionSet[0] != min(solutionSet): # Cycle solutionSet until the minimum is at index 0
            solutionSet = [solutionSet[-1],]+solutionSet[0:-1]
        solutionString = int(''.join(map(lambda n: str(n), solutionSet))) # Concat the values of solutionSet into an int
        if len(str(solutionString)) == 16:
            solutionStringList.append(solutionString)

print('answer:', max(solutionStringList))