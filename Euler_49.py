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

for i in range(1488, 10000):
    if isPrime(i):
        for j in range(1, 5000):
            if sorted(str(i)) == sorted(str(i+j)) == sorted(str(i+j+j)):
                if isPrime(i+j) and isPrime(i+j+j):
                    print(j)
                    print('answer:', str(i) + str(i+j) + str(i+j+j))
                    exit(0)