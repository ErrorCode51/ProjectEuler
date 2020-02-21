from decimal import Decimal, getcontext

getcontext().prec = 102 # Set the precision of Decimal objects, plus 2 to prevent rounding errors
answer = 0

for i in range(1, 100+1):
    d = Decimal(i).sqrt()
    if  d % 1 != 0: # If d is not an integer
        answer += sum((int(j) for j in str(d)[:-2].replace('.', '')))

print(answer)