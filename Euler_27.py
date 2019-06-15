import math

def isPrime(number):
    if number <= 1:
        return False
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        return False
    for i in range(7, int(math.sqrt(number) +1), 2):
        if number % i == 0:
            return False
    return True

a = 0
b = 0
primeStreak = 0

for x in range(-999, 1000):
    for y in range(-999, 1000):
        i = 0
        while True:
            if isPrime((i**2) + (x*i) + y):
                i += 1
            else:
                break
        if i > primeStreak:
            primeStreak = i
            a = x
            b = y

print('A:', a)
print('B:', b)
print('Streak:', primeStreak)
print('Product:', a*b)