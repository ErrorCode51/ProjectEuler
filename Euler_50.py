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

longestSum = 0
total = 0


for i in range(2, 1000000):
    if isPrime(i):
        numbers = [i]
        for j in range(i+1, 1000000):
            if isPrime(j):
                numbers.append(j)
                if isPrime(sum(numbers)):
                    if len(numbers) > longestSum:
                        longestSum = len(numbers)
                        total = sum(numbers)
            if sum(numbers) >= 1000000:
                break

print('Number of terms:', longestSum)
print('Sum:', total)

