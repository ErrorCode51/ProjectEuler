import math
# Quick and dirty prime test
def isPrime(number):
    if number <= 1:
        return False
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        return False
    for i in range(7, int(math.sqrt(number) +1), 2):
        if number % i == 0:
            return False
    return True

total = 4 # already counting all single digit prime numbers

for i in range(11, 1000000, 2):
    if isPrime(i):
        prime = True
        for x in range(1, len(str(i))):
            if not isPrime(int(str(i)[x:] + str(i)[:x])):
                prime = False
                break
        if prime:
            total += 1

print('total:', total)