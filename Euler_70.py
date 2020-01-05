import math

primes = [2,]
min = (10, 0)
x = 1

while True:
    x+=2
    sqrt = int(math.sqrt(x))
    isPrime = True
    # For phi(n) to be as close as possible to n, n needs to be the product of two prime numbers
    # This also greatly simplify's calculating phi(n), decreasing execution time
    for p in primes:
        if x%p == 0:
            isPrime = False
            break
        if p > sqrt:
            break
    if isPrime:
        for p in primes:
            i = x*p
            if i > 10_000_000:
                break
            phi = int(i * (1-(1/x)) * (1-(1/p)))
            if i/phi < min[0]:
                if sorted(str(i)) == sorted(str(phi)):
                    min = (i/phi, i)
        if primes[0]*x > 10_000_000:
            break
        primes.append(x)

print('answer:', min[1])