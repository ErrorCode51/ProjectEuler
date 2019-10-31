import math
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

size = 7 # the length of the sides
primes = 8
nrOfCorners = 13

rTop = 31
lTop = 37
lBottom = 43
rBottom = 49

while True:
    size += 2
    rTop = rBottom+size-1
    lTop = rTop+size-1
    lBottom = lTop+size-1
    rBottom = lBottom+size-1
    nrOfCorners += 4
    for x in [rTop, lTop, lBottom, rBottom]:
        if isPrime(x):
            primes +=1
    if primes/nrOfCorners < .1:
        break

print('answer:', size)