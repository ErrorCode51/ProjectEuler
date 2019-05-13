x = 1

def testNumber(number):
    #print("testing number ", number)
    for i in range(20):
        if (number % (i +1)):
            return 0
    return 1

print("Testing...")
while (1):
    if (testNumber(x)):
        break
    x += 1

print("finished: ", x)
