import math
# Quick and dirty prime test
def isPrime(number):
    if number <= 1:
        return False
    if number in [2, 3, 5]:
        return True
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        return False
    for i in range(7, int(math.sqrt(number) +1), 2):
        if number % i == 0:
            return False
    return True


highest = 0

def recursiveIteration(array, number):
    if len(array) == 0:
        if isPrime(number):
            global highest
            if number > highest:
                highest = number
    else:
        for d in array:
            newArray = array.copy()
            newArray.remove(d)
            recursiveIteration(newArray, (number*10)+d)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(9):
    recursiveIteration(numbers[:x+1], 0)

print('highest:', highest)
