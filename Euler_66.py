import math

"""
sources:
https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
https://en.wikipedia.org/w/index.php?title=Methods_of_computing_square_roots&oldid=927670414#Algorithm
"""

def isSquare(nr):
    return math.sqrt(nr).is_integer()


def getMinimumX(D):
    a0 = int(math.sqrt(D))
    m = 0
    d = 1
    a = a0
    n = 0
    convergentsList = []

    while True:
        # Calculate convergents
        if n == 0:
            convergents = (a0, 1)
        elif n == 1:
            convergents = ((a*a0)+1, a)
        else:
            convergents = ((a*convergentsList[-1][0])+(convergentsList[-2][0]), (a*convergentsList[-1][1])+(convergentsList[-2][1]))

        # Check to see if these convergents solve the equation
        if (convergents[0]**2) - (D*(convergents[1]**2)) == 1:
            return convergents[0]

        # The convergents did not solve the equation, calculating next coefficient
        convergentsList.append(convergents)
        n+=1
        m = (d * a) - m
        d = (D - (m ** 2)) / d
        a = int((math.sqrt(D) + m) / d)


def getSecondItem(list):
    return list[1]

print('answer:', max([(D, getMinimumX(D)) for D in range (1, 1000+1) if not isSquare(D)], key=getSecondItem)[0])