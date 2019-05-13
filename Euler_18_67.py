# this is the solutions to problem 18 and 67 by project euler

greatestPaths = []
with open('ProblemFiles/Problem_67.txt') as file:
    for line in file:
        newGreatestPath = []
        thisRow = [int(x.strip()) for x in line.split(' ')]
        if len(greatestPaths) == 0:
            newGreatestPath = thisRow
        else:
            for i in range(len(thisRow)):
                if i == 0:
                    newGreatestPath.append(thisRow[0] + greatestPaths[0])
                elif i == len(thisRow)-1:
                    newGreatestPath.append(thisRow[-1] + greatestPaths[-1])
                else:
                    if greatestPaths[i] > greatestPaths[i-1]:
                        newGreatestPath.append(thisRow[i] + greatestPaths[i])
                    else:
                        newGreatestPath.append(thisRow[i] + greatestPaths[i-1])
        print(newGreatestPath)
        greatestPaths = newGreatestPath

print('Highest: ', max(greatestPaths))
