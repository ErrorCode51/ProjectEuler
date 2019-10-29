from math import factorial

def nrOfSelections(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

answer = 0

for i in range(23, 100+1):
    for x in range(1, i):
        if nrOfSelections(i, x) > 1000000:
            answer +=1

print(answer)