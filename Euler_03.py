def isPrime(testNumber):
    x = 2
    while x < testNumber:
        if testNumber % x == 0:
            return(False)
        x += 1
    return(True)

value = 600851475143
largestPrime = 0
y = 1

while y < (value/2)+1:
    if value % y == 0:
        if isPrime(y):
            largestPrime = y
            print("New highest prime factor: " + str(largestPrime))
    y += 2

print("Largest prime factor: " + str(largestPrime))
