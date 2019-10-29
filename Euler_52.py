i = 1

def sortedList(nr):
    return sorted(str(nr))

while True:
    for x in range(5):
        if sortedList(i) != sortedList(i*(x+2)):
            break
        if x == 4:
            print(i)
            exit()
    i += 1
