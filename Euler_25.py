last = 1
secondLast = 1
index = 2

while last < 10**999:
    index += 1
    last, secondLast = last+secondLast, last

print(index)