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

i = 5

while True:
    if not isPrime(i):
        solved = True
        for x in range(1, i):
            if (x**2)*2 >= i:
                break
            if isPrime(i-((x**2)*2)):
                solved = False
                break
        if solved:
            print('answer:', i)
            exit(0)
    i += 2