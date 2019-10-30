nrOfLychrelNumbers = 0

def isLychrelNumber(number):
    for y in range(50):
       number = int(str(number)[::-1]) + number
       if str(number) == str(number)[::-1]:
           return False
    return True

for x in range(1, 10000):
    if isLychrelNumber(x):
        nrOfLychrelNumbers +=1


print('answer:', nrOfLychrelNumbers)