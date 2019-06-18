total = 0

def recursiveIteration(array, number):
    if len(array) == 0:
        numberStr = str(number)
        if len(numberStr) == 9:
            numberStr = '0' + numberStr
        if int(numberStr[1:4]) % 2 == 0:
            if int(numberStr[2:5]) % 3 == 0:
                if int(numberStr[3:6]) % 5 == 0:
                    if int(numberStr[4:7]) % 7 == 0:
                        if int(numberStr[5:8]) % 11 == 0:
                            if int(numberStr[6:9]) % 13 == 0:
                                if int(numberStr[7:10]) % 17 == 0:
                                    global total
                                    total += number
    else:
        for d in array:
            newArray = array.copy()
            newArray.remove(d)
            recursiveIteration(newArray, (number*10)+d)

recursiveIteration([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)

print('total:', total)
