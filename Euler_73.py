import math

answer = 0

for d in range(4, 12_000+1):
    for n in range(math.ceil(d/3), (d//2)+1):
        if math.gcd(n, d) == 1:
            answer +=1

print(answer)
