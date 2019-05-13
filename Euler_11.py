file = open("ProblemFiles/Problem_11.txt")
data = []

print("testing...")

highest = 0  # the highest number found so far

for line in file:
    data.append(line.split(" "))
    data[-1] = [int(number.strip("\n")) for number in data[-1]]
    #print(data[-1])


print("testing horizontal")
for x in range(17):
    for y in range(20):
        number = (data[y][x] * data[y][x +1] * data[y][x +2] * data[y][x +3])
        if(number > highest):
            highest = number

print("testing vertical")
for x in range(20):
    for y in range(17):
        number = (data[y][x] * data[y +1][x] * data[y +2][x] * data[y +3][x])
        if(number > highest):
            highest = number

print("testing vertical: NW SE")
for x in range(17):
    for y in range(17):
        number = (data[y][x] * data[y +1][x +1] * data[y +2][x +2] * data[y +3][x +3])
        if(number > highest):
            highest = number

print("testing vertical: NE SW")
for x in range(17):
    for y in range(3, 20):
        number = (data[y][x] * data[y -1][x +1] * data[y -2][x +2] * data[y -3][x +3])
        if(number > highest):
            highest = number

print("highest: ", highest)

