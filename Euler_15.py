
possibilities = []

size = 20

print("testing...")

for i in range(size+1):
    possibilities.append(1)

for y in range(size):
    for x in range(size):
        possibilities[size-x] = sum(possibilities[:size-x+1])

paths = possibilities[-1]
#paths += size




print("solved: ", paths)
