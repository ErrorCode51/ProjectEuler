import math

def isAbundant(number):
    sumOfDivisors = 1
    testingDevisor = 2
    sqrRoot = math.sqrt(number)
    if sqrRoot % 1 == 0:
        sumOfDivisors += sqrRoot
        sqrRoot -= 1
    while testingDevisor < sqrRoot:
        if number % testingDevisor == 0:
            sumOfDivisors += testingDevisor
            sumOfDivisors += number/testingDevisor
        testingDevisor += 1
    return (sumOfDivisors > number)

def isSumOfTwoAbundants(number):
    for i in range(12, int(number/2)+1):
        if isAbundant(i):
            if isAbundant(number-i):
                return True
    return False


total = 0

for i in range(1, 20162):
    print(i)
    if not isSumOfTwoAbundants(i):
        total += i

print('total:', total)