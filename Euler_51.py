import math
from itertools import combinations
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

i = 56994

while True:
    if isPrime(i):
        nrStr = str(i)
        for x in range(len(nrStr)):
            for y in combinations(range(len(nrStr)), x):
                arr = list(nrStr)
                primes = []
                for z in range(10):
                    for a in y:
                        arr[a] = str(z)
                    if arr[0] != '0':
                        nr = int(''.join(arr))
                        if isPrime(nr):
                            primes.append(nr)
                if len(primes) == 8:
                    print(y)
                    print(primes)
                    exit(0)
    i += 1


