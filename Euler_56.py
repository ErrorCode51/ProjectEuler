highest = 0

for x in range(1, 100):
    for y in range(1, 100):
        nr = int(x**y)
        nr = [int(n) for n in list(str(nr))]
        if sum(nr) > highest:
            highest = sum(nr)

print('highest:', highest)