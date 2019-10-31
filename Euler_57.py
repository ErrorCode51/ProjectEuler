numerator = 3
denominator = 2
answer = 0

for i in range(1, 1000):
    oldDenominator = denominator
    denominator += numerator
    numerator += 2*oldDenominator
    if len(str(numerator)) > len(str(denominator)):
        answer += 1

print('answer:', answer)