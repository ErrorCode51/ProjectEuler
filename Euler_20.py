def factorial(number):
    if number == 0:
        return 1
    output = 1
    for i in range(number):
        output *= i+1
    return output

print(sum([int(i) for i in str(factorial(100))]))