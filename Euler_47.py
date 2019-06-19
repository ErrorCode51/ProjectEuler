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

def getNrOfPrimeFactors(number):
    factors = 0
    for x in range(2, int(number/2)):
        if (number/x)%1 == 0:
            if isPrime(x):
                factors += 1
    return factors


i = 1
streak = 0

# TODO: make more efficient, this takes decades

while True:
    print(i)
    if getNrOfPrimeFactors(i) == 4:
        if getNrOfPrimeFactors(i+3) == 4:
            if getNrOfPrimeFactors(i+1) == 4 and getNrOfPrimeFactors(i+2) == 4:
                print('answer:', i)
                exit(0)
            else:
                i += 3
        else:
            i += 4
    else:
        i += 1

