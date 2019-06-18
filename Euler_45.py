def isPentagonNumber(number):
    if number < 1:
        return False
    i = 1
    step = 1000
    while True:
        pentaNumber = (i*((3*i)-1))/2
        if number == pentaNumber:
            return True
        elif pentaNumber > number:
            if step > 1:
                i -= step
                step /= 10
            else:
                return False
        i += 1

def isHexagonNumber(number):
    if number < 1:
        return False
    i = 1
    step = 10000
    while True:
        hexaNumber = i*((2*i)-1)
        if number == hexaNumber:
            return True
        elif hexaNumber > number:
            if step > 1:
                i -= step
                step /= 10
            else:
                return False
        i += step

i = 286
while True:
    tri = (i*(i+1))/2
    if isHexagonNumber(tri):
        if isPentagonNumber(tri):
            print('answer:', int(tri))
            break
    i += 1
