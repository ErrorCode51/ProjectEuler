#anwser: 142913828922

def isPrime(number):
    i = 2
    half = int(number/2)
    while (i < half):
        if not (number % i):
            return 0
        i += 1
    return 1

number = 2
print("testing...")
x = 3

while (x < 2000000):
    #print(x)
    if (isPrime(x)):
        number += x
        print(x)
    x += 2

print("solved: ", number)
