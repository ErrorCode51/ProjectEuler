def isPrime(number):
    for i in range(2, number):
        if not (number % i):
            return 0
    return 1

index = 0
prime = 0
x = 2

print("testing...")

while (index < 10001):
    if (isPrime(x)):
        index += 1
        prime = x
    x += 1

print("index: ", index)
print("number: ", prime)
