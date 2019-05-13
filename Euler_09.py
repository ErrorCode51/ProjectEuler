import math

for a in range(1000):
    for b in range(a +1, 1000):
        for c in range(b +1, 1000):
            if ((a + b + c) == 1000):
                if (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)):
                    print("solved:")
                    print("A: ", a)
                    print("B: ", b)
                    print("C: ", c)
                    print(a * b * c)
                    quit()