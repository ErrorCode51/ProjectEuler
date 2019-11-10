import math
from itertools import combinations, permutations
# As always, my quick and dirty prime test
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

primes = []
testingNumber = 1

nrOfPrimes = 5 # the number of primes that need to be concatenated, variable so it can be changes easily for testing


def getNextPrime():
    global testingNumber
    while True:
        testingNumber += 2
        if isPrime(testingNumber):
            return testingNumber


def concatsToPrimes(primes):
    for x in permutations(primes):
        if not isPrime(int(str(x[0]) + str(x[1]))):
            return False
    return True


while len(primes) < nrOfPrimes-1:
        primes.append(getNextPrime())


while True:
    newestPrime = getNextPrime()
    primes2 = [] # all primes that concatenate with newestPrime to produce a new prime
    for p in primes:
        if concatsToPrimes([p, newestPrime]):
            primes2.append(p)
    if len(primes2) >= nrOfPrimes-1:
        for x in combinations(primes2, nrOfPrimes-1):
            concatsAllToPrimes = True
            for y in permutations(x, 2):
                if not concatsToPrimes(y):
                    concatsAllToPrimes = False
                    break
                primes2 = x
            if concatsAllToPrimes:
                primes2 = list(x) + [newestPrime]
                print(primes2)
                print('total:', sum(primes2))
                exit()
    primes.append(newestPrime)

# TODO: this algorith currently takes around a minute and a half to complete, that is too long