print("Hello World")

a = 1
b = 2
total = 0

def isEven(number):
    if(number % 2 == 0):
        return(True)
    else:
        return(False)

while (b <= 4000000):
    if (isEven(b)):
        total += b
    print(b)

    a, b = b, a + b

print("Total: " + str(total))