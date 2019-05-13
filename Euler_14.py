
def steps(number):
    step = 0
    num = number
    while (num != 1):
        step += 1
        if (num % 2): #number is odd
            num = ((num *3) +1)
        else: #number is even
            num /= 2
    return step

print("testing...")

highest = 0
numHighest = 0


for x in range(1, 1000000):
    y = steps(x)
    if (y > highest):
        highest = y
        numHighest = x

print("number: ", numHighest)
print("steps: ", highest)
