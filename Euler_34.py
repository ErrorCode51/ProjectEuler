import numpy

def factorial(number):
    return numpy.prod(range(1, number+1))

total = 0
for i in range(3, 100000):
    if sum(factorial(int(x)) for x in str(i)) == i:
        print(i)
        total += i

print('total:', total)