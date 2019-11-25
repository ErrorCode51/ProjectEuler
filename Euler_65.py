# https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents

oldH = 8
oldK = 3

h = 11
k = 4


def coefficientGenerator(nrOfIterations, startingNumber=1):
    i=startingNumber
    while i < nrOfIterations:
        if i % 3 == 2:
            yield int((i/3)+1)*2
            i +=1
        else:
            yield 1
            i +=1


for i in coefficientGenerator(100, startingNumber=4):
    oldH, h = h, (i * h) + oldH
    oldK, k = k, (i * k) + oldK


print('100th convergent:', str(h) + '/' + str(k))
print('Sum of digits of numerator:', sum(int(x) for x in str(h)))

