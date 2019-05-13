import math

def calcDiv(num):
    i = 1
    half = (math.sqrt(num))
    x = 0
    while(i <= half):
        if ((num % i) == 0):
            x += 1
        i += 1
    x *= 2
    return x

def calcTriangle(num):
    value = 0
    for i in range(num + 1):
        value += (i)
    return value


print("calculating...")

number = 1
value = 1


while(1):
    print(value)
    if ((calcDiv(value)) > 500):
        break
    number += 1
    value += number




print("number: ", number)
print("value: ", value)
print("divisors: ", calcDiv(value))
