import math

sumSquares = 0 #de som van de kwadraten
squareSum = 0 #het kwadraad van de som

for i in range(100):
    sumSquares += math.pow(i+1, 2)


for i in range(100):
    squareSum += (i + 1)

squareSum = pow(squareSum, 2)


print("sumSquares: ", sumSquares)
print("squareSum: ", squareSum)
print("Difference: ", abs(squareSum - sumSquares))