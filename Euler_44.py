import array

def getPentaNumber(index):
    return int((index * ((3 * index) - 1)) / 2)

pArray = array.array('i')

for x in range(1, 5000):
    pArray.append(getPentaNumber(x))

def isPentagonNumber(number):
    if number < 1:
        return False
    global pArray
    for value in pArray:
        if number == value:
            return True
        if value > number:
            return False
    i = 1
    while True:
        pentaNumber = (i*((3*i)-1))/2
        if number == pentaNumber:
            return True
        elif pentaNumber > number:
            return False
        i += 1

i = 1
minimal = None

for x in range(1, 2500):
    px = getPentaNumber(x)
    for y in range(1, x):
        py = getPentaNumber(y)
        if isPentagonNumber(px-py):
            if isPentagonNumber(px+py):
                print(px, py)
                if minimal == None:
                    minimal = (px-py)
                elif minimal < px-py:
                    minimal = px-py

print('minimal:', minimal)