import math

numberSet = set()
MAX_SUM = 50_000_000


def is_prime(n):
    if n < 2:
        return False
    if n == 3:
        return True
    j = 3
    squareRootN = int(math.sqrt(n))+1
    while j < squareRootN:
        if (n / j).is_integer():
            return False
        j += 1
    return True


def get_next_prime(prevPrime):
    if prevPrime < 2:
        return 2
    if prevPrime == 2:
        return 3
    i = prevPrime + 2
    while True:
        if is_prime(i):
            return i
        i += 2


x = get_next_prime(0)
while (x**2) < MAX_SUM:
    y = get_next_prime(0)
    while (x**2) + (y**3) < MAX_SUM:
        z = get_next_prime(0)
        while (x**2) + (y**3) + (z**4) < MAX_SUM:
            numberSet.add((x**2) + (y**3) + (z**4))
            z = get_next_prime(z)
        y = get_next_prime(y)
    x = get_next_prime(x)

print('answer:', len(numberSet))