array = []

for x in range(2, 101):
    for y in range(2, 101):
        if x**y not in array:
            array.append(x**y)

print(len(array))