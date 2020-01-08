import math

# Source: https://en.wikipedia.org/wiki/Pythagorean_triple

def getCoprimes(nr):
    coprimes = []
    for x in range(1, nr):
        if math.gcd(x, nr) == 1:
            coprimes.append(x)
    return coprimes


MAX_LENGTH = 1_500_000
solutionsPenLength = [0] * MAX_LENGTH
m = 1

while True:
    coprimes = getCoprimes(m)
    for n in coprimes:
        if m%2 == 0 or n%2 ==0:
            triple = (m**2)-(n**2) + 2*m*n + (m**2)+(n**2)
            if triple > MAX_LENGTH:
                break
            multiplier = 1
            while triple*multiplier <= MAX_LENGTH:
                solutionsPenLength[(triple*multiplier)-1] +=1
                multiplier +=1

    if coprimes:
        if (m**2)-(coprimes[0]**2) + 2*m*coprimes[0] + (m**2)+(coprimes[0]**2) > MAX_LENGTH:
            break

    m += 1

print('answer:', solutionsPenLength.count(1))