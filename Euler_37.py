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

i = 11
found = 0
total = 0

while found < 11:
    if isPrime(i):
        truncatable = True
        for x in range(1, len(str(i))):
            if not isPrime(int(str(i)[x:])):
                truncatable = False
                break
        if truncatable:
            for x in range(1, len(str(i))):
                if not isPrime(int(str(i)[:x])):
                    truncatable = False
                    break
        if truncatable:
            print(i)
            total += i
            found += 1
    i += 1

print('total:', total)


