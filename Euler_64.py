import math

# https://en.wikipedia.org/w/index.php?title=Methods_of_computing_square_roots&oldid=927670414#Algorithm

# returns a list of all coefficients of a simple continued fraction of the square root of nr
def getCoefficients(nr):
    coefficients = []
    a0 = int(math.sqrt(nr))

    m = 0
    d = 1
    a = a0

    startingNumbers = None # required for detecting the end of the period

    while True:
        m = (d*a)-m
        d = (nr-(m**2))/d
        if d == 0: # this means that there is no period, because the square root of nr is a rational number
            return None
        a = int((math.sqrt(nr)+m)/d)
        if (m, d, a) == startingNumbers:
            break
        coefficients.append(a)
        if not startingNumbers:
            startingNumbers = (m, d, a)
    return (coefficients)


answer = 0

for i in range(1, 10000+1):
    coefficientsOfI = getCoefficients(i)
    if coefficientsOfI:
        if len(coefficientsOfI)%2 == 1:
            answer +=1


print('answer:', answer)

